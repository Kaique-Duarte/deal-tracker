from decimal import Decimal


class SteamService:
    def __init__(self):
        pass

    async def transform_json_to_list(self, data: dict):
        games = [item for item in data if item.get("price")]
        return [
            {
                "name": item["name"],
                "id": item["id"],
                "price": {
                    "initial": Decimal(str(item["price"]["initial"])) / Decimal("100"),
                    "final": Decimal(str(item["price"]["final"])) / Decimal("100"),
                },
            }
            for item in games[:3]
            
        ]
