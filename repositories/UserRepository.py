from sqlalchemy import select
from models.User import User
class UserRepository:
    
    def __init__(self, session):
        self.session = session
        
    def create_user(self, chat_id: int):
        user = User(chat_id=chat_id)
        
        self.session.add(user)

        return user
    
    def get_user_by_chat_id(self, chat_id: int):
        
        stmt = select(User).where(User.chat_id == chat_id)
        result = self.session.execute(stmt)
        
        return result.scalar()