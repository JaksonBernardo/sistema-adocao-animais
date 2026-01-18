
from fastapi import APIRouter, HTTPException
from app.schemas.GatoSchema import GatoCreate, GatoUpdate, GatoResponse
from app.services.GatoService import inserir_gato, atualizar_gato, deletar_gato, ler_gato

gato_router = APIRouter(
    prefix = "/animal/gato",
    tags = ["Gato"]
)


@gato_router.get("/{id_animal}", response_model = GatoResponse, status_code = 200)
async def pesquisar_gato(id_animal: int):

    try:

        gato = await ler_gato(id_animal)

        return gato
    
    except Exception as ex:

        raise HTTPException(status_code = 500, detail = f"Erro ao pesquisar gato: {str(ex)}")


@gato_router.post("/", response_model = GatoResponse, status_code = 201)
async def criar_gato(animal: GatoCreate):

    try:

        novo_animal = await inserir_gato(animal)

        return novo_animal
    
    except Exception as ex:

        raise HTTPException(status_code = 500, detail = f"Erro ao criar gato: {str(ex)}")

@gato_router.put("/{id_animal}", response_model = GatoResponse, status_code = 200)
async def alterar_gato(id_animal: int, animal: GatoUpdate):

    try:

        gato = await atualizar_gato(id_animal, animal)

        return gato

    except Exception as ex:

        raise HTTPException(status_code = 500, detail = f"Erro ao atualizar gato: {str(ex)}")


@gato_router.delete("/{id_animal}", status_code = 204)
async def excluir_gato(id_animal: int):

    try:

        await deletar_gato(id_animal)

    except Exception as ex:

        raise HTTPException(status_code = 500, detail = f"Erro ao excluir gato: {str(ex)}")
