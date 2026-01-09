
from fastapi import APIRouter
from app.schemas.GatoSchema import GatoCreate, GatoResponse
from app.services.GatoService import inserir_gato

gato_router = APIRouter(
    prefix = "/animal/gato",
    tags = ["Gato"]
)


@gato_router.post("/", response_model = GatoResponse, status_code = 201)
async def criar_gato(animal: GatoCreate):

    novo_animal = await inserir_gato(animal)

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


