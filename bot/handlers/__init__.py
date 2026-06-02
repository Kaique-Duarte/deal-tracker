from  bot.handlers.start_handler import router as start_handler
from bot.handlers.add_handler import router as add_handler
from bot.handlers.search_handler import router as search_handler
routers = [
    start_handler,
    add_handler,
    search_handler
]