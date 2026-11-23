from pydantic import BaseModel, ConfigDict

class BookBase(BaseModel):
    isbn: str
    title: str
    author: str
    category: str
    price: float
    total_copies: int
    available_copies: int

class BookCreate(BookBase):
    pass

class BookResponse(BookBase):
    id: int
    model_config = ConfigDict(from_attributes=True)