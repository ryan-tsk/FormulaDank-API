from fastapi import FastAPI
from routers import formuladank

app = FastAPI()

app.include_router(formuladank.router, prefix='/formuladank')

@app.get("/")
def main():
  return { "message" : "Server is live" }