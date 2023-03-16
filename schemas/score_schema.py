from pydantic import BaseModel

class Score(BaseModel):
    name: str
    song: str
    score: int