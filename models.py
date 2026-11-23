

from sqlalchemy import Column, Integer, String, Text, Float
from database import Base

class Books(Base):
    __tablename__ = 'Books'
    id = Column(Integer, primary_key=True, autoincrement=True)
    isbn = Column(String(100))
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    category = Column(String(250), nullable=False)
    price = Column(Float, nullable=False)
    total_copies= Column(Integer, nullable=False)
    available_copies= Column(Integer, nullable=False)



