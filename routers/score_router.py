import requests
from fastapi import APIRouter, HTTPException
from schemas import score_schema
from typing import List

router = APIRouter()

scores = []


@router.post("/scores/")
async def create_score(score: score_schema.Score):
    scores.append(score)
    return score


@router.get("/scores/", response_model=List[score_schema.Score])
async def read_scores():
    return scores


@router.get("/search_songs")
async def search_songs(query: str):
    response = requests.get(f"https://api.deezer.com/search?q={query}")
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, detail=response.text)
    return response.json()["data"]
