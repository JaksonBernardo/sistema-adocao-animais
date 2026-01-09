from pydantic import BaseModel
from app.schemas.AnimalSchema import AnimalBase, AnimalResponse


class CachorroCreate(AnimalBase):
    necessidade_passeio: bool
    independencia: bool


class CachorroResponse(AnimalResponse):
    necessidade_passeio: bool
    independencia: bool
