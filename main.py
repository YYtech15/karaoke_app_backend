from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import music_router, user_router
from schemas import music_schema, user_schema

app = FastAPI(
    title='カラオケApp',
    description='昔のトレンド楽曲などを検索可能',
)
app.include_router(music_router.router)
app.include_router(user_router.router)

origins = [
    "http://localhost:8080",
    "https://karaoke-app-three.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index():
    return {"message": "Hello"}


@app.get("/hello")
def index():
    return {"message": "Hello World"}
