# app/main.py
from fastapi import FastAPI
from app.routes.CachorroRouters import cachorro_router
from app.routes.GatoRouters import gato_router

app = FastAPI()

app.include_router(cachorro_router)
app.include_router(gato_router)