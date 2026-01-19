from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, id: int, especie: str, raca: str, nome: str,
                 sexo: str, idade: int, porte: str, temperamento: str, 
                 status: str) -> None:
        
        self._id = id
        self._especie = especie
        self._raca = raca
        self._nome = nome
        self._sexo = sexo
        self._idade = idade
        self._porte = porte
        self._temperamento = temperamento
        self._status = status

    @property
    def id(self) -> int: return self._id

    @property
    def especie(self) -> str: return self._especie

    @property
    def raca(self) -> str: return self._raca

    @property
    def nome(self) -> str: return self._nome

    @property
    def sexo(self) -> str: return self._sexo

    @property
    def idade(self) -> int: return self._idade

    @property
    def porte(self) -> str: return self._porte

    @property
    def temperamento(self) -> str: return self._temperamento

    @property
    def status(self) -> str: return self._status

    @id.setter
    def id(self, id: int) -> None:

        if id < 0:
            raise ValueError("O ID do animal não pode ser negativo.")
        
        self._id = id

    @especie.setter
    def especie(self, especie: str) -> None:
        self._especie = especie

    @raca.setter
    def raca(self, raca: str) -> None:
        self._raca = raca

    @nome.setter
    def nome(self, nome: str) -> None:

        if not nome:
            raise ValueError("O nome do animal não pode ser vazio.")
        
        self._nome = nome

    @sexo.setter
    def sexo(self, sexo: str) -> None:

        if sexo not in ['M', 'F']:
            raise ValueError("O sexo deve ser 'M' para macho ou 'F' para fêmea.")
        
        self._sexo = sexo

    @idade.setter
    def idade(self, idade: int) -> None:

        if idade < 0:
            raise ValueError("A idade do animal não pode ser negativa.")
        
        self._idade = idade

    @porte.setter
    def porte(self, porte: str) -> None:

        if porte not in ['P', 'M', 'G']:
            raise ValueError("O porte deve ser 'P' para pequeno, 'M' para médio ou 'G' para grande.")
        
        self._porte = porte

    @temperamento.setter
    def temperamento(self, temperamento: str) -> None:

        self._temperamento = temperamento

    @status.setter
    def status(self, novo_status: str) -> None:
        
        transicoes_validas = {
            "DISPONIVEL": ["RESERVADO", "INADOTAVEL"],
            "RESERVADO": ["ADOTADO", "DISPONIVEL"], 
            "ADOTADO": ["DEVOLVIDO"],
            "DEVOLVIDO": ["QUARENTENA", "DISPONIVEL", "INADOTAVEL"],
            "QUARENTENA": ["DISPONIVEL", "INADOTAVEL"],
            "INADOTAVEL": [] 
        }

        if novo_status not in ["DISPONIVEL", "RESERVADO", "ADOTADO", "DEVOLVIDO", "QUARENTENA", "INADOTAVEL"]:
            
            raise ValueError("Status indisponível.")
            
        if novo_status not in transicoes_validas.get(self._status, []):
            
            raise ValueError(f"Transição ilegal: Não é possível mudar de '{self._status}' para '{novo_status}'.")
        
        self._status = novo_status

    def custo_adocao(self, estrategia_calculo: 'EstrategiaTaxa') -> float:
        
        return estrategia_calculo.calcular(self)

    

    
