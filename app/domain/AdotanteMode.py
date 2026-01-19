
from app.domain.PessoaModel import Pessoa

class Adotante(Pessoa):

    def __init__(self, id: int, nome: str, idade: int, moradia: str, 
                 area_util: float, experiencia_pets: bool, tem_crianca: bool, outros_animais: bool,
                 renda_mensal: float) -> None:
        
        super().__init__(id, nome, idade, moradia, area_util, experiencia_pets, tem_crianca, outros_animais)
        
        self._renda_mensal = renda_mensal

    @property
    def renda_mensal(self) -> float: 

        return self._renda_mensal

    @renda_mensal.setter
    def renda_mensal(self, renda_mensal: float) -> None:

        if renda_mensal <= 0:

            raise ValueError("Renda mensal não pode ser negativa ou zerada")
        
        self._renda_mensal = renda_mensal


