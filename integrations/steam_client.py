import httpx

class SteamClient:
    
    def __init__(self):
        pass
    async def consultar_api(self, term: str):
        params = { 'term': term, 'cc': 'br', 'l': 'portuguese'}
        url = "https://store.steampowered.com/api/storesearch"
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url=url, params=params)
                return response.json()
        except Exception as e:
             raise e
        
