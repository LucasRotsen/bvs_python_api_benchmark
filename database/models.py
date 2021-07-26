from sqlalchemy import Column, Integer, String

from database.config import Base


class Dog(Base):
    __tablename__ = "dog"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
