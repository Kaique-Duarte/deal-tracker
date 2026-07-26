from models.games import Games
from sqlalchemy import select
from decimal import Decimal
class GamesRepository: 
    def __init__(self, session):
        self.session = session
    
    
    async def get_game_from_search_name(self, term: str):
        
        stmt = select(Games).where(Games.search_name.ilike(f"%{term}%"))
        result = self.session.execute(stmt)    
        return result.scalars().all()
    
    
    async def create_game(self, s_id: int, name: str, search_name: str, last_pr: Decimal):
        game = Games(steam_app_id=s_id, name=name, search_name=search_name, last_price=last_pr)
        
        self.session.add(game)
        
        return game
        
    
    


    