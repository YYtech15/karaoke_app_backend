from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from typing import List
from schemas import music_schema
import cruds.music_crud as music_crud
from db import get_db

router = APIRouter()


@router.get("/musics", response_model=List[music_schema.Music])
async def list_musics(db: AsyncSession = Depends(get_db)):
    return await music_crud.get_musics_all(db)


@router.post("/musics", response_model=music_schema.MusicCreateResponse)
async def create_music(
    music_body: music_schema.MusicCreate, db: AsyncSession = Depends(get_db)
):
    return await music_crud.create_music(db, music_body)


@router.put("/musics/{music_id}", response_model=music_schema.MusicCreateResponse)
async def update_music(
    music_id: int, music_body: music_schema.MusicCreate, db: AsyncSession = Depends(get_db)
):
    music = await music_crud.get_music(db, music_id=music_id)
    if music is None:
        raise HTTPException(status_code=404, detail="music not found")

    return await music_crud.update_music(db, music_body, original=music)


@router.delete("/musics/{music_id}", response_model=None)
async def delete_music(music_id: int, db: AsyncSession = Depends(get_db)):
    music = await music_crud.get_music(db, music_id=music_id)
    if music is None:
        raise HTTPException(status_code=404, detail="music not found")

    return await music_crud.delete_music(db, original=music)
