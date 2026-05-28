from database.db.Base import Base
from sqlalchemy import Column, Integer, String, Float



class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    chat_id = Column(Integer, unique=True)
    nome = Column(String(50))

    def __init__(self, id, preco):
        self.id = id
        self.preco = preco
        
