from repositories.user_repository import UserRepository
class UserServices: 
    def __init__(self, session):
        self.user_repository = UserRepository(session)
        self.session = session   
        
    def register_user(self, chat_id: int, username: str):
        user_exists = self.user_repository.get_user_by_chat_id(chat_id)
        
        if user_exists:
            raise Exception("Usuario já Existe") # tratar erro
        
        user = self.user_repository.create_user(chat_id, username)
        self.session.commit()
        
        return user