from models import UserWatchGames
from sqlalchemy.sql import select


class WatchRepository:
    def __init__(self, session):
        self.session = session

    def get_watch(self, userID: int, gameID: int):
        stmt = select(UserWatchGames).where(
            UserWatchGames.user_id == userID,
            UserWatchGames.game_id == gameID
        )
        result = self.session.execute(stmt)
        return result.scalar()

    def create_watch_game(self, userID: int, gameID: int):
        watch = UserWatchGames(user_id=userID, game_id=gameID)

        self.session.add(watch)
        return watch
