from database.base import Base
from sqlalchemy import Integer, Column, ForeignKey
class UserWatchGames(Base):
    
    __tablename__ = 'user_watch_games'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True)
    game_id = Column(Integer, ForeignKey("games.id", ondelete="CASCADE"), nullable=False, unique=True)
    last_notified_discont = Column(Integer)
    