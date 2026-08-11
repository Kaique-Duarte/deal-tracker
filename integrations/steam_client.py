import httpx

class SteamClient:
    
    def __init__(self):
        pass
    async def consult_api(self, search: str | int):
        params = { 'term': search, 'cc': 'br', 'l': 'portuguese'}
        url = "https://store.steampowered.com/api/storesearch"
     
        async with httpx.AsyncClient() as client:
            response = await client.get(url=url, params=params)
            response.raise_for_status()
            return response.json()['items']
        
        
