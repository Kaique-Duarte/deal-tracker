from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import BotCommand
from bot.handlers import routers
class DealTrackerBot:
    def __init__(self, token):
        self.bot = Bot(token=token)
        self.dp = Dispatcher()
        for router in routers:
            self.dp.include_router(router)
        
    
    async def run(self):
            await self.bot.set_my_commands([
                BotCommand(command="start", description="inicia o Bot"),
                BotCommand(command="search", description="EX: /search Nome do Jogo"),
                BotCommand(command="add", description="Adiciona O jogo")
            ])
            
            await self.dp.start_polling(self.bot)

        
    
        
        
        
