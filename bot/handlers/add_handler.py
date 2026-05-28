from aiogram import types, Router
from aiogram.filters import Command

router = Router()

@router.message(Command("add"))
async def add_handler(message: types.Message): 
    await message.answer("Opa Você Adicinou UM jogo kkk")