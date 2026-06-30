from aiogram import types, Router
from aiogram.filters import Command, CommandObject
from services.games_service import GamesService
# from database.engine import sessionLocal
router = Router()
games_service = GamesService()

@router.message(Command('search'))
async def search_handler(message: types.Message, command:CommandObject):
    games_name = command.args
    games = await games_service.search_game(games_name)
    print(message.text)
    texto = "\n\n".join(
    f"🎮 {item['name']}\n"
    f"💰 R$ {item['price']['final']}"
    for item in games
)   
    print(texto, flush=True)
    await message.answer(texto)#
    
    
    
    
    
    