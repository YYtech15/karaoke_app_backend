from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from typing import List, Tuple, Optional
from datetime import datetime
import models.music_model as music_model
import schemas.music_schema as music_schema


async def create_music(
    db: AsyncSession, music_create: music_schema.MusicCreate
) -> music_model.Music:
    music = music_model.Music(**music_create.dict())
    db.add(music)
    await db.commit()
    await db.refresh(music)
    return music


async def get_musics_all(db: AsyncSession) -> List[Tuple[int, str, str, str, datetime, datetime]]:
    result: Result = await db.execute(
        select(
            music_model.Music.id,
            music_model.Music.title,
            music_model.Music.singer,
            music_model.Music.level,
            music_model.Music.created_at,
            music_model.Music.updated_at,
        )
    )
    return result.fetchall()


async def get_music(db: AsyncSession, music_id: int) -> Optional[music_model.Music]:
    result: Result = await db.execute(
        select(music_model.Music).filter(music_model.Music.id == music_id)
    )
    music: Optional[Tuple[music_model.Music]] = result.first()
    return music[0] if music is not None else None
    # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す


async def update_music(
    db: AsyncSession, music_create: music_schema.MusicCreate, original: music_model.Music
) -> music_model.Music:
    original.title = music_create.title
    original.singer = music_create.singer
    original.level = music_create.level
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_music(db: AsyncSession, original: music_model.Music) -> None:
    await db.delete(original)
    await db.commit()
