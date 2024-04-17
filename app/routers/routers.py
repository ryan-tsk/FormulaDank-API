from fastapi import APIRouter
from .formuladank import router as formuladank

router = APIRouter()

router.include_router(formuladank, prefix="/formuladank", tags=["formula dank"])