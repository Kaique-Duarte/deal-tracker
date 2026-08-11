from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from scheduler.jobs import check_prices

scheduler = AsyncIOScheduler()



async def start_scheduler(bot):
    scheduler.add_job(
        check_prices,
        args=[bot],
        trigger=IntervalTrigger(hours=1),
        id="check_games_prices"
    )


    scheduler.start()