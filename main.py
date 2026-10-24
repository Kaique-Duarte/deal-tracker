import asyncio

from sqlalchemy.exc import OperationalError, SQLAlchemyError

from bot.deal_tracker_bot import DealTrackerBot
from config.settings import TOKEN
from database.base import Base
from database.engine import engine
from scheduler.scheduler import start_scheduler
from config.logger import setup_logging

async def main():
    setup_logging(arquivo="erros.log")
    try:
        Base.metadata.create_all(bind=engine)
    except OperationalError as e:
        print(f"Erro de Conexão: {e}", flush=True)
    except SQLAlchemyError as e:
        print(f"Erro No Banco: {e}", flush=True)
    except Exception as e:
        print(f"Erro: {e}", flush=True)
    bot = DealTrackerBot(TOKEN)
    await start_scheduler(bot.bot)
    print("BOT Iniciado Com Sucesso :)", flush=True)
    await bot.run()


if __name__ == "__main__":
    asyncio.run(main())
