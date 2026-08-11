from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import Command, CommandObject
from services import GamesService, WatchService
from database.engine import sessionLocal
from utils.build_game_result import build_game_result
from utils.normalize import normalize
router = Router()


@router.message(Command("search"))
async def search_handler(message: Message, command: CommandObject):
    games_name = normalize(command.args)
    with sessionLocal() as session:
        games_service = GamesService(session=session)
        games = await games_service.search_game(games_name)
    print(games, flush=True)
    builder = InlineKeyboardBuilder()
    print(games, flush=True)
    for game in games:
        print(game, flush=True)
        builder.button(text=game['name'], callback_data=f"game:{game['id']}")
    
    builder.adjust(1)    

    custom_message = await build_game_result(games)
   

    await message.answer(
        f" {custom_message}\n Selecione uma das três opções disponíveis ou realize uma nova busca.\n OBS: ao clicar no botão o jogo será acompanhado!",
        reply_markup=builder.as_markup(),
    )
    
    

    
@router.callback_query(F.data.startswith('game:'))
async def callback_handler(callback: CallbackQuery):
    print(callback.data , flush=True)
    appid = int(callback.data.split(':')[1])
    with sessionLocal() as session:
        watch_service = WatchService(session)
        await watch_service.watch_game(steam_app_id=appid, chat_id=callback.from_user.id)

    await callback.message.answer("✅ Jogo adicionado ao acompanhamento!")

       
       
 

 