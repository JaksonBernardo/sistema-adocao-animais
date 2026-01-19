from pydantic import BaseModel


class PessoaBase(BaseModel):
    nome: str
    idade: int
    moradia: str
    area_util: float
    experiencia_pets: bool
    tem_crianca: bool
    outros_animais: bool


class PessoaResponse(PessoaBase):

    class Config:

        from_attributes = True