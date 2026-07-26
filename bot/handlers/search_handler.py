from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command, CommandObject
from services.games_service import GamesService
from database.engine import sessionLocal
from utils.normalize import normalize
router = Router()


@router.message(Command("search"))
async def search_handler(message: Message, command: CommandObject):
    games_name = normalize(command.args)
    with sessionLocal() as session:
        games_service = GamesService(session=session)
        games = await games_service.search_game(games_name)

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="1° Opção", callback_data="opção_1"),
                InlineKeyboardButton(text="2° Opção", callback_data="opção_2"),
                InlineKeyboardButton(text="3° Opção", callback_data="opção_3"),
            ]
        ]
    )

   

    await message.answer(
        f" {games}\n Selecione uma das três opções disponíveis ou realize uma nova busca.",
        reply_markup=keyboard,
    )
    
    
@router.callback_query(F.data == "opção_1")
async def handle_opcao_1(callback: CallbackQuery):
    print("OPÇÂO UMMMMMMMMMMMMM", flush=True)
    
@router.callback_query(F.data == "opção_2")
async def handle_opcao_2(callback: CallbackQuery):
    print("OPÇÂO Doisssssss", flush=True)
    
@router.callback_query(F.data == "opção_3")
async def handle_opcao_3(callback: CallbackQuery):
    print("OPÇÂO Trêssssss", flush=True)
       
       
 

 