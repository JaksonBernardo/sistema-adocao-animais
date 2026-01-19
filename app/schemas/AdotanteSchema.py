from pydantic import BaseModel
from app.schemas.PessoaSchema import PessoaBase, PessoaResponse

class AdotanteCreate(PessoaBase):
    renda_mensal: float

class AdotanteResponse(PessoaResponse):
    nome: str
    idade: int

class AdotanteUpdate(BaseModel):
    nome: str
    idade: int
    moradia: str
    area_util: float
    experiencia_pets: bool
    tem_crianca: bool
    outros_animais: bool
    renda_mensal: float