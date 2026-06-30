from sqlalchemy import select
from models.user import User
class UserRepository:
    
    def __init__(self, session):
        self.session = session
        
    
    def get_user_by_chat_id(self, chat_id: int):
        
        stmt = select(User).where(User.chat_id == chat_id)
        result = self.session.execute(stmt)
        
        return result.scalar()
    
    def create_user(self, chat_id: int, username: str):
        user = User(chat_id=chat_id, username=username)
        
        self.session.add(user)

        return user