from pydantic import BaseModel
from typing import Literal

class AnimalBase(BaseModel):
    raca: str
    nome: str
    sexo: Literal["M", "F"]
    idade: int
    porte: Literal["P", "M", "G"]
    temperamento: str
    status: Literal[
        "DISPONIVEL",
        "RESERVADO",
        "ADOTADO",
        "DEVOLVIDO",
        "QUARENTENA",
        "INADOTAVEL"
    ]


class AnimalResponse(AnimalBase):
    id: int
    especie: str

    class Config:
        from_attributes = True
