from aiogram import F, Router
from aiogram.filters import Command, CommandObject
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from sqlalchemy.exc import OperationalError, SQLAlchemyError

from database.engine import sessionLocal
from exceptions import GameNotFoundError, WatchAlreadyExistsError, UserNotFoundError
from services import GamesService, WatchService
from utils.build_game_result import build_game_result
from utils.normalize import normalize
import logging

logger = logging.getLogger(__name__)

MSG_ERROR = "🔧 Estamos com problemas no servidor, por favor aguarde e tente novamente mais tarde..."
MSG_GAME_NOT_FOUND = "🔍 Jogo não encontrado, tente novamente...\n\nDica: Tente escrever exatamente como está escrito na Steam."
router = Router()


@router.message(Command("search"))
async def search_handler(message: Message, command: CommandObject):
    games_name = normalize(command.args)
    with sessionLocal() as session:
        games_service = GamesService(session=session)
        try:
            games = await games_service.search_game(games_name)
            print(games, flush=True)
            builder = InlineKeyboardBuilder()
            print(games, flush=True)
            for game in games:
                print(game, flush=True)
                builder.button(text=game["name"], callback_data=f"game:{game['id']}")
            builder.adjust(1)

            custom_message = await build_game_result(games)
            await message.answer(
                f" {custom_message}\n Selecione uma das três opções disponíveis ou realize uma nova busca.\nOBS: ao clicar no botão o jogo será acompanhado!",
                reply_markup=builder.as_markup(),
            )
        except GameNotFoundError:
            games_service.session.rollback()
            await message.answer(MSG_GAME_NOT_FOUND)
        except OperationalError:
            games_service.session.rollback()
            await message.answer(MSG_ERROR)
            logger.warning("Caiu o Banco!")
        except SQLAlchemyError:
            games_service.session.rollback()
            await message.answer(MSG_ERROR)
            logger.error("Erro no Banco!")
        except Exception:
            games_service.session.rollback()
            await message.answer(MSG_ERROR)
            logger.exception("Erro Inesperado!")


@router.callback_query(F.data.startswith("game:"))
async def callback_handler(callback: CallbackQuery):
    print(callback.data, flush=True)
    appid = int(callback.data.split(":")[1])
    
    with sessionLocal() as session:
        
        try:

            watch_service = WatchService(session)
            await watch_service.watch_game(
                steam_app_id=appid, chat_id=callback.from_user.id
            )

            await callback.message.answer("✅ Jogo adicionado ao acompanhamento!")

        except UserNotFoundError:
            watch_service.session.rollback()
            await callback.message.answer("Como vc consigui chegar aqui sem ter aceitado os termos?")
        except WatchAlreadyExistsError:
            watch_service.session.rollback()
            await callback.message.answer("Você já está acompanhando essa jogo. 👀")
        except OperationalError:
            watch_service.session.rollback()
            await callback.message.answer(MSG_ERROR)
            logger.warning("Caiu o banco!")
        except SQLAlchemyError:
            watch_service.session.rollback()
            await callback.message.answer(MSG_ERROR)
            logger.error("Erro no banco!")
        except Exception:
            watch_service.session.rollback()
            await callback.message.answer(MSG_ERROR)
            logger.exception("Erro Inesperado!")