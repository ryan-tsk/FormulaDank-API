from fastapi import APIRouter
from requests import request

router = APIRouter()

@router.get("/")
async def test_get():
  return ""

@router.get("/path")
async def test_get_2():
  return ""