from datetime import datetime
from schemas.music_schema import Music
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime
    # favorites: list[Music] = []

    class Config:
        orm_mode = True