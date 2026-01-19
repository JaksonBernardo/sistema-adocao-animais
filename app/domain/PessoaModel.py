from abc import ABC
from config import SETTINGS_INFO

class Pessoa(ABC):

    def __init__(self, id: int, nome: str, idade: int, moradia: str, 
                 area_util: float, experiencia_pets: bool, tem_crianca: bool, outros_animais: bool) -> None:
        
        self._id = id
        self._nome = nome
        self._idade = idade
        self._moradia = moradia
        self._area_util = area_util
        self._experiencia_pets = experiencia_pets
        self._tem_crianca = tem_crianca
        self._outros_animais = outros_animais


    @property
    def id(self) -> int: return self._id

    @property
    def nome(self) -> str: return self._nome

    @property
    def idade(self) -> int: return self._idade

    @property
    def moradia(self) -> str: return self._moradia

    @property
    def area_util(self) -> float: return self._area_util

    @property
    def experiencia_pets(self) -> bool: return self._experiencia_pets

    @property
    def tem_crianca(self) -> bool: return self._tem_crianca

    @property
    def outros_animais(self) -> bool: return self._outros_animais

    @nome.setter
    def nome(self, nome: str) -> None:

        if not nome:

            raise ValueError("Nome não pode ser vazio")
        
        self._nome = nome

    @idade.setter
    def idade(self, idade: int) -> None:

        idade_minima = SETTINGS_INFO["idade_minima"]

        if idade < idade_minima:

            raise ValueError(f"Idade deve ser maior ou igual a {idade_minima} anos")
        
        self._idade = idade

    @moradia.setter
    def moradia(self, moradia: str) -> None:

        if moradia not in ["casa", "apto"]:

            raise ValueError("Moradia deve ser 'casa' ou 'apto'")

        self._moradia = moradia

    @area_util.setter
    def area_util(self, area_util: float) -> None:

        area_minima = SETTINGS_INFO["area_util_minima"]

        if area_util <= area_minima:

            raise ValueError(f"Área útil deve ser maior que {area_minima}")
        
        self._area_util = area_util

    @experiencia_pets.setter
    def experiencia_pets(self, experiencia_pets: bool) -> None:

        self._experiencia_pets = experiencia_pets

    @tem_crianca.setter
    def tem_crianca(self, tem_crianca: bool) -> None:

        self._tem_crianca = tem_crianca

    @outros_animais.setter
    def outros_animais(self, outros_animais: bool) -> None:

        self._outros_animais = outros_animais

    
