
from fastapi import APIRouter, HTTPException
from app.schemas.CachorroSchema import CachorroCreate, CachorroUpdate, CachorroResponse
from app.services.CachorroService import inserir_cachorro, atualizar_cachorro, deletar_cachorro, ler_cachorro 

cachorro_router = APIRouter(
    prefix = "/animal/cachorro",
    tags = ["Cachorro"]
)

@cachorro_router.get("/{id_animal}", response_model = CachorroResponse, status_code = 200)
async def pesquisar_cachorro(id_animal: int):

    try:

        cachorro = await ler_cachorro(id_animal)

        return cachorro
    
    except Exception as ex:

        raise HTTPException(status_code = 500, detail = f"Erro ao pesquisar cachorro: {str(ex)}")
    

@cachorro_router.post("/", response_model = CachorroResponse, status_code = 201)
async def criar_cachorro(animal: CachorroCreate):

    try:

        novo_animal = await inserir_cachorro(animal)

        return novo_animal
    
    except Exception as ex:

        raise HTTPException(status_code = 500, detail = f"Erro ao criar cachorro: {str(ex)}")
    

@cachorro_router.put("/{id_animal}", response_model = CachorroResponse, status_code = 200)
async def alterar_cachorro(id_animal: int, animal: CachorroUpdate):

    try:

        cachorro = await atualizar_cachorro(id_animal, animal)

        return cachorro

    except Exception as ex:

        raise HTTPException(status_code = 500, detail = f"Erro ao atualizar cachorro: {str(ex)}")
    

@cachorro_router.delete("/{id_animal}", status_code = 204)
async def excluir_cachorro(id_animal: int):

    try:

        await deletar_cachorro(id_animal)

    except Exception as ex:

        raise HTTPException(status_code = 500, detail = f"Erro ao excluir cachorro: {str(ex)}")


