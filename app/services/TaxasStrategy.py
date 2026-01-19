from abc import ABC, abstractmethod

class EstrategiaTaxa(ABC):
    @abstractmethod
    def calcular(self, animal) -> float:
        pass

class TaxaFilhote(EstrategiaTaxa):
    def calcular(self, animal) -> float:
        return 100.00 

class TaxaIdoso(EstrategiaTaxa):
    def calcular(self, animal) -> float:
        return 20.00 
        
class TaxaPadrao(EstrategiaTaxa):
    def calcular(self, animal) -> float:
        taxa = 50.00
        if animal.raca and animal.raca.lower() != "srd":
            taxa += 50.00
        return taxa