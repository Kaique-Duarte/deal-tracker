from database.Base import Base
from sqlalchemy import Column, Integer, String, Float, BigInteger



class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(BigInteger, unique=True)
    

    
        
