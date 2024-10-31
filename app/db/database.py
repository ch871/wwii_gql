from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.settings.config import DB_URL

engine = create_engine(DB_URL)
session_maker = sessionmaker(bind=engine)

Base = declarative_base()



