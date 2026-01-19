from pydantic import BaseModel
from typing import Optional, Literal
from app.schemas.AnimalSchema import AnimalBase, AnimalResponse

class CachorroCreate(AnimalBase):
    necessidade_passeio: bool
    independencia: bool

class CachorroUpdate(BaseModel):
    raca: Optional[str]
    nome: Optional[str]
    sexo: Optional[Literal["M", "F"]]
    idade: Optional[int]
    porte: Optional[Literal["P", "M", "G"]]
    temperamento: Optional[str]
    status: Optional[Literal[
        "DISPONIVEL",
        "RESERVADO",
        "ADOTADO",
        "DEVOLVIDO",
        "QUARENTENA",
        "INADOTAVEL"
    ]]

    necessidade_passeio: Optional[bool]
    independencia: Optional[bool]


class CachorroResponse(AnimalResponse):
    necessidade_passeio: bool
    independencia: bool
