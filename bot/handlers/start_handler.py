from aiogram import types, Router
from aiogram.filters import Command
from database.Engine import sessionLocal
from services.UserServices import UserServices
router =  Router()


@router.message(Command('start'))
async def start_handler(message: types.Message):
    await message.answer("""Salve 😄 eu sou teu Bot de Alerta de Preços da Steam 💸🎮
Eu fico de olho nas promoções e te aviso quando aquele jogo fica em oferta ou bate um preço bom.
Sem estresse, sem ficar caçando desconto: eu faço o trabalho sujo por você 😎""")
    with sessionLocal() as session:
        user_service = UserServices(session)
        user_service.register_user(message.chat.id)
    