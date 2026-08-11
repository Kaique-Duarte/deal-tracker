from services import SteamService, GamesService
from repositories import WatchRepository
from exceptions import WatchGamesNotFoundError, GameNotFoundError
from decimal import Decimal
from utils.discount import calculate_discount
class SchedulerService:

    def __init__(self, session, bot):
        self.watch_repository = WatchRepository(session)
        self.game_service = GamesService(session)
        self.steam_service = SteamService()
        self.session = session
        self.bot = bot
    async def check_games_price(self):
        result = self.watch_repository.get_all_watch_games()
        if not result:
            raise WatchGamesNotFoundError()
        
        for game, watch, user in result:

            data = await self.game_service.search_game_for_app_id(game.steam_app_id)
           
           
            normal_price = data[0]['price']['initial']
            current_price = data[0]['price']['final']
       
    
            
           
            if current_price < normal_price and current_price != watch.last_notified_discont:
                
                discount = await calculate_discount(normal_price, current_price)

                message = await self.warn_user_watch_game(game.name, normal_price, current_price, discount, game.steam_app_id)



                await self.bot.send_message(chat_id=user.chat_id, text=message)
                   
                
                                        

                self.watch_repository.update_last_notified_discount(watch_id=watch.id, current_price=current_price)
               
                self.session.commit()
                continue
                
            print("Ignorando....", flush=True)
           
                
            
          
            
    async def warn_user_watch_game(self, game_name: str, normal_price: Decimal, current_price: str, discont: Decimal, app_id: int):
        return f"""🔥 OFERTA ENCONTRADA!

🎮 {game_name}

💰 De R$ {normal_price} por R$ {current_price}
📉 Desconto de {discont}%

👉 Aproveite enquanto o preço está baixo!
🔗 https://store.steampowered.com/app/{app_id}"""