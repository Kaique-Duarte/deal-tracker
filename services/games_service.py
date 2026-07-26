from integrations.steam_client import SteamClient
from services.steam_service import SteamService
from repositories.games_repository import GamesRepository
from sqlalchemy.exc import SQLAlchemyError


class GamesService:
    def __init__(self, session=None):
        self.session = session
        self.steam_client = SteamClient()
        self.steam_service = SteamService()
        self.games_repository = GamesRepository(session)

    async def search_game(self, term: str):
        try:
            game_exists = await self.games_repository.get_game_from_search_name(term)

            if game_exists:
                game_exists_list = [
                    {"name": game_exist.name, "id": game_exist.steam_app_id}
                    for game_exist in game_exists
                ]
                return await self.steam_service.build_game_result(game_exists_list)

            data = await self.steam_client.consult_api(term)
            if data:
                records = await self.steam_service.transform_json_to_list(data)

                return await self.steam_service.build_game_result(records)

        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Erro ao Consultar O banco de dados: {e}", flush=True)
        except (ValueError, TypeError, KeyError) as e:
            print(f"Erro de dados/input: {e}", flush=True)
        except Exception as e:  # noqa: BLE001
            print(f"Erro: {e}", flush=True)

    async def register_game(self, record: str, term: str):

        try:
            game = await self.games_repository.create_game(
                record["id"], record["name"], term, record["price"]["final"]
            )
            self.session.commit()
            return game
        except SQLAlchemyError as e:
            self.session.rollback()
            print(f"Erro ao Criar jogo: {e}", flush=True)
        except (ValueError, TypeError, KeyError) as e:
            print(f"Erro de dados/input: {e}")
        except Exception as e:  # noqa: BLE001
            print(f"Erro: {e}", flush=True)
