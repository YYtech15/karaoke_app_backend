from typing import List
from fastapi import APIRouter
from schemas import music_schema

router = APIRouter()


@router.get("/musics", response_model=List[music_schema.Music])
async def list_musics():
    return [music_schema.Music(id=1, title="桜")]


@router.post("/musics", response_model=music_schema.MusicCreateResponse)
async def create_music_list(music_id: int, music_body: music_schema.MusicCreate):
    return music_schema.MusicCreateResponse(id=music_id, **music_body.dict())


@router.put("/musics/{music_id}", response_model=music_schema.MusicCreateResponse)
async def update_musics_list(music_id: int, music_body):
    return music_schema.MusicCreateResponse(id=music_id, **music_body.dict())


@router.delete("/musics/{music_id}", response_model=None)
async def delete_musics_list(music_id: int):
    return
