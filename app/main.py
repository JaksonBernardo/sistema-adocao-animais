# app/main.py
from fastapi import FastAPI
from app.routes.CachorroRouters import animal_router

app = FastAPI()

app.include_router(animal_router)