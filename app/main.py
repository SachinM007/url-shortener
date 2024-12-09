from fastapi import FastAPI, HTTPException
from app.models import URLMapping
from app.database import database
from app.utils import generate_short_id

app = FastAPI()


@app.post("/shorten/")
async def shorten_url(original_url: str):
    if not original_url.startswith("http"):
        raise HTTPException(status_code=400, detail="Invalid URL format")

    short_id = generate_short_id()
    database[short_id] = URLMapping(original_url=original_url, short_id=short_id)
    return {"short_url": f"http://short.ly/{short_id}"}


@app.get("/{short_id}")
async def redirect_url(short_id: str):
    mapping = database.get(short_id)
    if not mapping:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"original_url": mapping.original_url}

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the URL Shortener API!"}
