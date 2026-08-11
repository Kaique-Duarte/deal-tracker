from config.settings import TOKEN
import asyncio

from bot.deal_tracker_bot import DealTrackerBot
from database.engine import engine
from database.base import Base
from models.user import User
from models.games import Games
from models.user_watch_games import UserWatchGames
from scheduler.scheduler import start_scheduler

async def main():
    Base.metadata.create_all(bind=engine)
    bot = DealTrackerBot(TOKEN)
    await start_scheduler(bot.bot)
    print("BOT Iniciado Com Sucesso :)")
    await bot.run()
    
if __name__ == '__main__':
    asyncio.run(main())