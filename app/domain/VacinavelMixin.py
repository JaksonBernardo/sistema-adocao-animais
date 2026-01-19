from typing import List, Dict
from datetime import date

class VacinavelMixin:
    def __init__(self):
        self._historico_vacinas: List[Dict] = []

    def registrar_vacina(self, nome_vacina: str, data_aplicacao: date = None) -> None:
        """Adiciona uma vacina ao histórico do animal."""
        if data_aplicacao is None:
            data_aplicacao = date.today()
            
        registro = {
            "vacina": nome_vacina,
            "data": data_aplicacao.isoformat()
        }
        self._historico_vacinas.append(registro)
        print(f"Vacina '{nome_vacina}' registrada com sucesso.")

    def listar_vacinas(self) -> List[Dict]:
        """Retorna todas as vacinas tomadas."""
        return self._historico_vacinas
        
    @property
    def vacinado(self) -> bool:
        """Propriedade calculada: retorna True se tiver ao menos uma vacina"""
        return len(self._historico_vacinas) > 0