from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field

class MusicBase(BaseModel):
    title: str = Field(None, example="イマジネーション")
    artist: str = Field(None, example="SPYAIR")
    level: str = Field("レベル1",description="level1")

class Music(MusicBase):
    id: int
    created_at: datetime
    updated_at: datetime
    

    class Config:
        orm_mode = True

class MusicCreate(MusicBase):
    pass

class MusicCreateResponse(MusicCreate):
    id: int

    class Config:
        orm_mode = True
        # orm_mode = Trueを設定
        # Pydanticモデルの属性を
        # id = data["id"] だけでなく id = data.id でも参照可能に
