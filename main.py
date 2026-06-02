from config.settings import TOKEN
import asyncio

from bot.deal_tracker_bot import DealTrackerBot
from database.engine import engine
from database.base import Base
async def main():
    Base.metadata.create_all(engine)
    
    bot = DealTrackerBot(TOKEN)
    print("BOT Iniciado Com Sucesso :)")
    await bot.run()
if __name__ == '__main__':
    asyncio.run(main())