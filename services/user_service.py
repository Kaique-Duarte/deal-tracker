from repositories.user_repository import UserRepository
class UserServices: 
    def __init__(self, session):
        self.user_repository = UserRepository(session)
        self.session = session   
        
    def register_user(self, chat_id: int):
        user_exists = self.user_repository.get_user_by_chat_id(chat_id)
        
        if user_exists:
            raise Exception("Usuario já Existe")
        
        user = self.user_repository.create_user(chat_id)
        self.session.commit()
        
        return user