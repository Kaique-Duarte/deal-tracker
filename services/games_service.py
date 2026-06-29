from integrations.steam_client import SteamClient
from services.steam_service import SteamService
class GamesService:
    
    def __init__(self):
        self.steam_client = SteamClient()
        self.steam_service = SteamService()
    
    
    async def search_game(self, term: str):
        data = await self.steam_client.consult_api(term)
        return await self.steam_service.build_game_result(data)
    
    
    
    ###a
    