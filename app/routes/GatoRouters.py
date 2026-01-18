
from fastapi import APIRouter, HTTPException
from app.schemas.GatoSchema import GatoCreate, GatoUpdate, GatoResponse
from app.services.GatoService import inserir_gato, atualizar_gato

gato_router = APIRouter(
    prefix = "/animal/gato",
    tags = ["Gato"]
)


@gato_router.post("/", response_model = GatoResponse, status_code = 201)
async def criar_gato(animal: GatoCreate):

    try:

        novo_animal = await inserir_gato(animal)

        return novo_animal
    
    except Exception as ex:

        raise HTTPException(status_code = 500, detail = f"Erro ao criar gato")

@gato_router.put("/{id_animal}", response_model = GatoResponse, status_code = 200)
async def alterar_gato(id_animal: int, animal: GatoUpdate):

    try:

        gato = await atualizar_gato(id_animal, animal)

        return gato

    except Exception as ex:

        raise HTTPException(status_code = 500, detail = f"Erro ao atualizar gato")

