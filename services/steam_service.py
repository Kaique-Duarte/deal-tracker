from decimal import Decimal
class SteamService:
    def __init__(self):
        pass

    async def build_game_result(self, games_list: list):

        return "\n\n".join(f"🎮 {item['name']}\n" for item in games_list)

    async def transform_json_to_list(self, data: dict):

      return [
    {
        "name": item["name"],
        "id": item["id"],
        "price": {
            "initial": Decimal(str(item["price"]["initial"])),
            "final": Decimal(str(item["price"]["final"])),
        },
    }
    for item in data[:3]
]
