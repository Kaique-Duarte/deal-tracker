from config.settings import TOKEN
import asyncio
from aiogram import Bot, Dispatcher, types
from bot.DealTrackerBot import DealTrackerBot
from database.Engine import engine
from database.Base import Base
async def main():
    Base.metadata.create_all(engine)
    
    
        
    
        
    bot = DealTrackerBot(TOKEN)
    print("BOT Iniciado Com Sucesso :)")
    await bot.run()
if __name__ == '__main__':
    asyncio.run(main())