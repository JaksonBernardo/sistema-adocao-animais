
from .AnimalModel import Animal
from .VacinavelMixin import VacinavelMixin
from .AdestravelMixin import AdestravelMixin

class Cachorro(Animal, VacinavelMixin, AdestravelMixin):

    def __init__(self, id: int, raca: str, nome: str, sexo: str, 
                 idade: int, porte: str, temperamento: str, status: str, 
                 necessidade_passeio: bool, independencia: bool) -> None:
        
        super().__init__(id, "Cachorro", raca, nome,
                         sexo, idade, porte, temperamento, 
                         status)
        
        self._necessidade_passeio = necessidade_passeio
        self._independencia = independencia

    @property
    def necessidade_passeio(self) -> bool: return self._necessidade_passeio

    @property
    def independencia(self) -> bool: return self._independencia

    @necessidade_passeio.setter
    def necessidade_passeio(self, necessidade_passeio: bool) -> None:
        self._necessidade_passeio = necessidade_passeio

    @independencia.setter
    def independencia(self, independencia: bool) -> None:
        self._independencia = independencia

    
