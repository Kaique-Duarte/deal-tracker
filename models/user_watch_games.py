from database.base import Base
from sqlalchemy import Integer, Column, ForeignKey
class UserWatchGames(Base):
    
    __tablename__ = 'user_watch_games'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    game_id = Column(Integer, ForeignKey("games.id", ondelete="CASCADE"), nullable=False)
    last_notified_discont = Column(Integer(), nullable=True)
    