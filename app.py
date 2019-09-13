from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
import json


app = FastAPI()

# Database Connection
db_client = MongoClient('localhost', 27017)
db = db_client.test_db
# users = mydb["users"]
posts = db.posts

# Database Collection Model


@app.post("/api/posts")
async def create_post(new_post: dict):
    post = await posts.insert_one(new_post)
    print(post)
    return new_post


@app.get("/api/posts/{post_id}")
async def get_post(post_id: int):
    return {
        "id": post_id,
        "title": "something",
        "description": "`1234567890 lorem ipsum one two three bla bal bla..."
    }


@app.get('/api/posts')
async def get_params(skip: int, limit: int):
    return {
        "skip": skip,
        "limit": limit
    }
