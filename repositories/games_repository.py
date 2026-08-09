from models.games import Games
from sqlalchemy import select
from decimal import Decimal
class GamesRepository: 
    def __init__(self, session):
        self.session = session
    
    async def get_game_from_app_id(self, steam_app_id: int):
        
        stmt = select(Games).where(Games.steam_app_id == steam_app_id)
        result = self.session.execute(stmt)
        return result.scalar()
        
    async def get_game_from_name(self, term: str):
        
        stmt = select(Games).where(Games.name.ilike(f"%{term}%"))
        result = self.session.execute(stmt)    
        return result.scalars().all()
    
    async def create_game(self, s_id: int, name: str, last_pr: Decimal):
        game = Games(steam_app_id=s_id, name=name, last_price=last_pr)
        
        self.session.add(game)
        
        return game
        
    
    


    