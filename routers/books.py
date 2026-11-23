from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic_extra_types import isbn
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db

router = APIRouter(
    prefix="/books",
    tags=["books"],
)


@router.get("/", response_model=List[schemas.BookResponse])
def get_all_books(db: Session = Depends(get_db)):
    return db.query(models.Books).all()


# int route MUST come before the {name} route
@router.get("/{id:int}", response_model=schemas.BookResponse)
def get_book_by_id(id: int, db: Session = Depends(get_db)):
    book = db.query(models.Books).filter(models.Books.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.get("/{name}", response_model=List[schemas.BookResponse])
def get_book_by_name(name: str, db: Session = Depends(get_db)):
    return (
        db.query(models.Books)
        .filter(models.Books.title.ilike(f"%{name}%"))
        .all()
    )

@router.get("/{isbn}", response_model=schemas.BookResponse)
def get_book_by_name(isbn: str, db: Session = Depends(get_db)):
    book = db.query(models.Books).filter(models.Books.isbn == isbn).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book