

class SteamService:
    def __init__(self):
       pass

        
    async def build_game_result(self, data: dict):

        return [
            {
                "name": item["name"],
                "id": item["id"],
                "price": {
                    "initial": item["price"]["initial"],
                    "final": item["price"]["final"],
                },
            }
        for item in data[:3]
        ]
