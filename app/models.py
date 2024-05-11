from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Text

from app.core.db import Base


class Cat(Base):
    __tablename__ = 'cats'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer(), nullable=False)
    description = Column(Text)

    def __repr__(self):
        return f'[{self.id}] {self.name}'
