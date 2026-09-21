from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


app = FastAPI(title="Library API")


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    genre: str = Field(min_length=1)


class Book(BookInput):
    id: int


books = [
    Book(id=1, title="1984", author="George Orwell", genre="dystopian"),
    Book(id=2, title="Pride and Prejudice", author="Jane Austen", genre="romance"),
]


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/books", response_model=list[Book])
def list_books(genre: str | None = None):
    """Return all books, optionally filtered by genre."""
    if genre is None:
        return books
    return [book for book in books if book.genre.lower() == genre.lower()]


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_input: BookInput):
    """Create a book and assign the next available ID."""
    next_id = max((book.id for book in books), default=0) + 1
    book = Book(id=next_id, **book_input.model_dump())
    books.append(book)
    return book


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_input: BookInput):
    for index, book in enumerate(books):
        if book.id == book_id:
            updated_book = Book(id=book_id, **book_input.model_dump())
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return None
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")