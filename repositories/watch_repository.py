from models import UserWatchGames, Games, User
from sqlalchemy.sql import select, update
from decimal import Decimal

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
    def get_all_watch_games(self):
        stmt = select(Games, UserWatchGames, User).join(UserWatchGames, UserWatchGames.game_id == Games.id).join(User, User.id == UserWatchGames.user_id)
        
        result = self.session.execute(stmt)
        return result.all()
        
    def create_watch_game(self, userID: int, gameID: int):
        watch = UserWatchGames(user_id=userID, game_id=gameID)

        self.session.add(watch)
        return watch
    def update_last_notified_discount(self, watch_id: int, current_price: Decimal):
        stmt = update(UserWatchGames).where(UserWatchGames.id == watch_id).values(last_notified_discont=current_price)
        self.session.execute(stmt)
    
    
