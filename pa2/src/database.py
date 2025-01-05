from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv
import os

load_dotenv()

connect_args = {"check_same_thread": False}
engine = create_engine(os.getenv("DATABASE_URL"), connect_args=connect_args)

class Base(DeclarativeBase):
    pass

Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
