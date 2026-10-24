from database.engine import sessionLocal
from services import SchedulerService
from exceptions import WatchGamesNotFoundError
from sqlalchemy.exc import SQLAlchemyError, OperationalError
import logging
logger = logging.getLogger(__name__)



async def check_prices(bot):

    with sessionLocal() as session:
        try:

            scheduler_service = SchedulerService(session, bot)
            await scheduler_service.check_games_price()

        except WatchGamesNotFoundError:
            scheduler_service.session.rollback()
        except OperationalError:
            logger.warning("Caiu o Banco!")
        except SQLAlchemyError:
            logger.error("Erro No Banco!")
        except Exception:
            logger.exception("Erro Inesperado!")