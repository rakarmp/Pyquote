from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# KOnfigurasi cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Mengizinkan semua origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"]
)

# Koneksi ke MongoDB
client = MongoClient("ISI DENGAN URL MONGODB")
db = client["quote_db"]
collection = db["quotes"]

class Quote(BaseModel):
    id: str
    text: str
    author: str

@app.get("/")
def get_info():
    return {
        "info": "Pyquote by rakarmp (Zyarexx)",
        "message_author": "Make sure you don't forget to change the url to connect to the mongodb database, Happy to use!",
        "message": "to use pyquote please go to /docs"
        }

@app.get("/quotes", response_model=List[Quote])
def get_quotes():
    quotes = list(collection.find())
    return quotes

@app.get("/quotes/random", response_model=Quote)
def get_random_quote():
    quotes = list(collection.find())
    if quotes:
        random_quote = random.choice(quotes)
        return random_quote
    return {"error": "Quote Not Found"}

@app.get("/quotes/{quote_id}", response_model=Quote)
def get_quote(quote_id: str):
    quote = collection.find_one({"id": quote_id})
    if quote:
        return quote
    return {"error": "Quote not found"}

@app.post("/quotes", response_model=Quote)
def create_quote(quote: Quote):
    collection.insert_one(quote.dict())
    return quote

@app.put("/quotes/{quote_id}", response_model=Quote)
def update_quote(quote_id: str, quote: Quote):
    updated_quote = collection.find_one_and_update(
        {"id": quote_id},
        {"$set": quote.dict()},
        return_document=True
    )
    if updated_quote:
        return updated_quote
    return {"error": "Quote not found"}

@app.delete("/quotes/{quote_id}")
def delete_quote(quote_id: str):
    result = collection.delete_one({"id": quote_id})
    if result.deleted_count > 0:
        return {"message": "Quote deleted"}
    return {"error": "Quote not found"}
