
from fastapi import APIRouter
from app.schemas.CachorroSchema import CachorroCreate, CachorroResponse
from app.services.CachorroService import inserir_cachorro

cachorro_router = APIRouter(
    prefix = "/animal/cachorro",
    tags = ["Cachorro"]
)


@cachorro_router.post("/", response_model = CachorroResponse, status_code = 201)
async def criar_cachorro(animal: CachorroCreate):

    novo_animal = await inserir_cachorro(animal)

    return {
        "id": novo_animal.id,
        "especie": novo_animal.especie,
        "raca": novo_animal.raca,
        "nome": novo_animal.nome,
        "sexo": novo_animal.sexo,
        "idade": novo_animal.idade,
        "porte": novo_animal.porte,
        "temperamento": novo_animal.temperamento,
        "status": novo_animal.status,
        "necessidade_passeio": novo_animal.necessidade_passeio,
        "independencia": novo_animal.independencia
    }
