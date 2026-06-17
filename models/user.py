from database.base import Base
from sqlalchemy import Column, Integer, BigInteger, DateTime, String
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger, unique=True)
    username = Column(String(50), nullable=False)
    create_at = Column(DateTime, server_default=func.now())

    
        
