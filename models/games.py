from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, String
from sqlalchemy.sql import func

from database.base import Base


class Games(Base):
    __tablename__ = "games"
    id = Column(Integer, primary_key=True, autoincrement=True)
    steam_app_id = Column(BigInteger, unique=True)
    name = Column(String(100))
    last_price = Column(Numeric(10, 2))
    create_at = Column(DateTime, server_default=func.now())
    update_at = Column(DateTime, server_default=func.now(), server_onupdate=func.now())
    # coloca quantos reais de desc
