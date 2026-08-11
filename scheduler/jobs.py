from services import SchedulerService
from database.engine import sessionLocal


async def check_prices(bot):
    
    with sessionLocal() as session:
        scheduler_service = SchedulerService(session, bot)
        await scheduler_service.check_games_price()
    