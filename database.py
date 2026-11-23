from sqlalchemy import create_engine
from urllib.parse import quote_plus

from sqlalchemy.orm import sessionmaker, declarative_base


password = quote_plus("Sandesh123!")
DATABASE_URL = f"mysql+pymysql://myuser:{password}@localhost:3306/library_db"
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



