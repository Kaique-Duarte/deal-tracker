from database.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Numeric, Boolean
from sqlalchemy.sql import func
class Games(Base):
    
    __tablename__ = "games"
    id = Column(Integer, primary_key=True, autoincrement=True)
    steam_app_id = Column(Integer)
    name = Column(String(50))
    original_price = Column(Numeric)
    current_price = Column(Numeric)
    discont = Column(Integer)
    on_sale = Column(Boolean)
    create_at = Column(DateTime, server_default=func.now())
    
   