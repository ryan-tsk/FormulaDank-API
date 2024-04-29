from fastapi import APIRouter
from requests import request
from service import api

router = APIRouter()

@router.get("/")
async def test_get():
  x = api.get_meme('formuladank')
  return x


@router.get("/path")
async def test_get_2():
  return ""