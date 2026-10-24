from exceptions import GameNotFoundError, GamesAlreadyExistsError
from integrations.steam_client import SteamClient
from repositories.games_repository import GamesRepository
from services import SteamService


class GamesService:
    def __init__(self, session=None):
        self.session = session
        self.steam_client = SteamClient()
        self.steam_service = SteamService()
        self.games_repository = GamesRepository(session)

    async def search_game(self, search: str):

        game_exists = await self.games_repository.get_game_from_name(search)

        if game_exists:
            return [
                {
                    "name": game_exist.name,
                    "id": game_exist.steam_app_id,
                    "price": {"final": game_exist.last_price},
                }
                for game_exist in game_exists
            ]

        data = await self.steam_client.consult_api(search)
        if data:
            print(data, flush=True)
            return await self.steam_service.transform_json_to_list(data)

        raise GameNotFoundError()


    async def search_game_for_app_id(self, app_id: int):
        data = await self.steam_client.consult_api(app_id)
        if data:
            return await self.steam_service.transform_json_to_list(data)

        raise GameNotFoundError()

    async def register_game(self, record: list):

        game = await self.games_repository.create_game(
            record[0]["id"], record[0]["name"], record[0]["price"]["final"]
        )
        self.session.commit()

        if game:
            return game

        raise GamesAlreadyExistsError

    # except SQLAlchemyError as e:
    #     self.session.rollback()
    #     print(f"Erro ao Criar jogo: {e}", flush=True)
