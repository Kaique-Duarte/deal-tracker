from sqlalchemy import BigInteger, Column, DateTime, Integer, String
from sqlalchemy.sql import func

from database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger, unique=True)
    username = Column(String(50), nullable=False)
    create_at = Column(DateTime, server_default=func.now())
    update_at = Column(DateTime, server_default=func.now(), server_onupdate=func.now())
