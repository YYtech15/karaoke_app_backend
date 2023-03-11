from fastapi import Depends, APIRouter, HTTPException
from schemas import user_schema


router = APIRouter()

@router.post("/signup")
async def signup():
    pass

@router.post("/login")
async def login():
    pass