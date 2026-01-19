from typing import List

class AdestravelMixin:
    def __init__(self):
        self._comandos_aprendidos: List[str] = []
        self._adestrado: bool = False

    def aprender_comando(self, comando: str) -> None:
        """Ensina um novo comando ao animal"""
        if comando not in self._comandos_aprendidos:
            self._comandos_aprendidos.append(comando)
            self._adestrado = True
            print(f"Comando '{comando}' aprendido!")
        else:
            print(f"O animal já sabe o comando '{comando}'.")

    def listar_comandos(self) -> List[str]:
        return self._comandos_aprendidos

    @property
    def is_adestrado(self) -> bool:
        return self._adestrado