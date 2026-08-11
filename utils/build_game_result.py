async def build_game_result(games_list: list):
        
        return "\n\n".join(f"🎮 {item['name']} R$ {item['price']['final']:.2f}\n".replace(".", ",") for item in games_list)