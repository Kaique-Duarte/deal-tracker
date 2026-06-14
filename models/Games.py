from database.base import Base
from sqlalchemy import Column, Integer, String

class Games(Base):
    
    __tablename__ = "games"
    id = Column(Integer, primary_key=True, autoincrement=True)
    steam_app_id = Column(Integer)
    name = Column(String(50))
    
   