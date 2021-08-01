from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from api.config import POSTGRES_USERNAME, POSTGRES_PASSWORD, POSTGRES_DATABASE

SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USERNAME}:{POSTGRES_PASSWORD}@localhost/{POSTGRES_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=50, max_overflow=-1)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
