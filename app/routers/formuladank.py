from fastapi import APIRouter
from requests import request
from ..service import meme_service

router = APIRouter()

@router.get("/")
async def test_get():
  x = meme_service.get_meme()
  return x


@router.get("/path")
async def test_get_2():
  return ""