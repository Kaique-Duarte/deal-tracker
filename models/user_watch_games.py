from sqlalchemy import Column, ForeignKey, Integer, Numeric

from database.base import Base


class UserWatchGames(Base):
    __tablename__ = "user_watch_games"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(
        Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    game_id = Column(
        Integer, ForeignKey("games.id", ondelete="CASCADE"), nullable=False
    )
    last_notified_discont = Column(Numeric(10, 2), nullable=True)
