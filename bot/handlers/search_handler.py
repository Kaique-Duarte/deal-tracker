from aiogram import types, Router
from aiogram.filters import Command

router = Router()

@router.message(Command('search'))
async def search_handler(message: types.Message):
    await message.answer("Não Achei Nada kkkkkk")