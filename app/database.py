from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.settings import DB_URL

DB_URL = DB_URL

engine = create_engine(url=DB_URL, echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False)


class Base(DeclarativeBase):
	pass
