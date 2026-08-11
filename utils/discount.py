from decimal import Decimal
async def calculate_discount(normal_price: Decimal, current_price: Decimal):
    
    
    return round(((normal_price - current_price) / normal_price) * 100)  