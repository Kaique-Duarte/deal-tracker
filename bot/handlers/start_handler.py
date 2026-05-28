from aiogram import types, Router
from aiogram.filters import Command
router =  Router()


@router.message(Command('start'))
async def start_handler(message: types.message):
    await message.answer("""Salve 😄 eu sou teu Bot de Alerta de Preços da Steam 💸🎮
Eu fico de olho nas promoções e te aviso quando aquele jogo fica em oferta ou bate um preço bom.
Sem estresse, sem ficar caçando desconto: eu faço o trabalho sujo por você 😎""")