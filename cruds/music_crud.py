from sqlalchemy.ext.asyncio import AsyncSession

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
