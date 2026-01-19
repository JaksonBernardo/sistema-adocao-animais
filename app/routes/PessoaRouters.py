from fastapi import APIRouter, HTTPException, status
from app.schemas.PessoaSchema import PessoaBase, PessoaResponse
from app.services.PessoaService import criar_pessoa, obter_pessoa, atualizar_pessoa, remover_pessoa

pessoa_router = APIRouter(
    prefix="/pessoas",
    tags=["Pessoa"]
)

@pessoa_router.post("/", response_model=PessoaResponse, status_code=status.HTTP_201_CREATED)
async def criar(data: PessoaBase):

    try:

        return await criar_pessoa(data)

    except Exception as ex:

        raise HTTPException(status_code=500, detail=f"Erro ao criar pessoa: {str(ex)}")


@pessoa_router.get("/{id_pessoa}", response_model=PessoaResponse)
async def buscar(id_pessoa: int):

    try:

        pessoa = await obter_pessoa(id_pessoa)
        if not pessoa:
            raise HTTPException(status_code=404, detail="Pessoa não encontrada")
        return pessoa

    except Exception as ex:

        raise HTTPException(status_code=500, detail=f"Erro ao buscar pessoa: {str(ex)}")


@pessoa_router.put("/{id_pessoa}", response_model=PessoaResponse)
async def atualizar(id_pessoa: int, data: PessoaBase):

    try:

        return await atualizar_pessoa(id_pessoa, data)
    
    except Exception as ex:

        raise HTTPException(status_code=500, detail=f"Erro ao atualizar pessoa: {str(ex)}")


@pessoa_router.delete("/{id_pessoa}", status_code=status.HTTP_204_NO_CONTENT)
async def deletar(id_pessoa: int):

    try:

        await remover_pessoa(id_pessoa)

    except Exception as ex:

        raise HTTPException(status_code=500, detail=f"Erro ao deletar pessoa: {str(ex)}")
