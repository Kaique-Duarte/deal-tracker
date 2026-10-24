import os
from pathlib import Path

from dotenv import load_dotenv

# Carrega .env da raiz do projeto
dotenv_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path)

TOKEN = os.getenv("TOKEN")
DB_URL = os.getenv("DB_URL")
