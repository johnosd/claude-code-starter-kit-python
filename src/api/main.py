from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel

from src.api.example import get_books, process_results

app = FastAPI(
    title="Google Books API",
    description="Busca livros via Google Books API",
    version="1.0.0",
)


class Book(BaseModel):
    title: str
    author: list[str]


@app.get("/books", response_model=list[Book])
def search_books(
    q: str = Query(..., description="Termo de busca"),
    page: int = Query(1, ge=1, description="Número da página"),
) -> list[Book]:
    """Busca livros na Google Books API."""
    data = get_books(query=q, page=page)

    if "items" not in data:
        raise HTTPException(status_code=404, detail="Nenhum livro encontrado.")

    return [Book(**book) for book in process_results(data)]
