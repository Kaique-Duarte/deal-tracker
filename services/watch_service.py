from repositories import WatchRepository, UserRepository, GamesRepository
from services import GamesService
from exceptions import UserNotFoundError, GameNotFoundError, WatchAlreadyExistsError

class WatchService:
    def __init__(self, session):
        self.session = session
        self.user_repository = UserRepository(session=session)
        self.games_repository = GamesRepository(session=session)
        self.watch_repository = WatchRepository(session=session)
        self.game_service = GamesService(session)
    async def watch_game(self, steam_app_id: int, chat_id: int):
        user_exists = self.user_repository.get_user_by_chat_id(chat_id)
        if not user_exists:
            raise UserNotFoundError()
        game_exists = await self.games_repository.get_game_from_app_id(steam_app_id)
        if not game_exists:
           record = await self.game_service.search_game_for_app_id(app_id=steam_app_id)
           game_exists = await self.game_service.register_game(record) 

        watch_exists = self.watch_repository.get_watch(userID=user_exists.id, gameID=game_exists.id)
        if watch_exists:
            raise WatchAlreadyExistsError()
            
        watch = self.watch_repository.create_watch_game(userID=user_exists.id, gameID=game_exists.id)
        self.session.commit()
        return watch
