from fastapi import APIRouter, HTTPException, status
from app.schemas.AdotanteSchema import AdotanteCreate, AdotanteResponse, AdotanteUpdate
from app.services.AdotanteService import criar_adotante, obter_adotante, atualizar_adotante, remover_adotante

adotante_router = APIRouter(
    prefix="/adotantes",
    tags=["Adotante"]
)

@adotante_router.post("/", response_model=AdotanteResponse, status_code=status.HTTP_201_CREATED)
async def criar(data: AdotanteCreate):

    try:

        return await criar_adotante(data)

    except Exception as ex:

        raise HTTPException(status_code=500, detail=f"Erro ao criar adotante: {str(ex)}")

@adotante_router.get("/{id_pessoa}", response_model=AdotanteResponse)
async def buscar(id_pessoa: int):

    try:

        adotante = await obter_adotante(id_pessoa)
        if not adotante:
            raise HTTPException(status_code=404, detail="Adotante não encontrado")
        return adotante
    
    except Exception as ex:

        raise HTTPException(status_code=500, detail=f"Erro ao buscar adotante: {str(ex)}")


@adotante_router.put("/{id_pessoa}", response_model=AdotanteResponse)
async def atualizar(id_pessoa: int, data: AdotanteUpdate):

    try:

        return await atualizar_adotante(id_pessoa, data)
    
    except Exception as ex:

        raise HTTPException(status_code=500, detail=f"Erro ao atualizar adotante: {str(ex)}")


@adotante_router.delete("/{id_pessoa}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar(id_pessoa: int):

    try:

        await remover_adotante(id_pessoa)

    except Exception as ex:

        raise HTTPException(status_code=500, detail=f"Erro ao deletar adotante: {str(ex)}")
