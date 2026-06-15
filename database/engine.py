from config.settings import DB_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import psycopg2

engine = create_engine(DB_URL)

sessionLocal = sessionmaker(bind=engine)