# app/services/PessoaService.py

from app.domain.PessoaModel import Pessoa
from app.schemas.PessoaSchema import PessoaBase
from app.repositories.PessoaRepo import inserir_pessoa, buscar_pessoa_por_id, atualizar_pessoa, deletar_pessoa

async def criar_pessoa(data: PessoaBase) -> Pessoa:
    pessoa = Pessoa(
        id=0,
        nome=data.nome,
        idade=data.idade,
        moradia=data.moradia,
        area_util=data.area_util,
        experiencia_pets=data.experiencia_pets,
        tem_crianca=data.tem_crianca,
        outros_animais=data.outros_animais
    )

    pessoa_id = await inserir_pessoa(pessoa)
    pessoa._id = pessoa_id

    return pessoa


async def obter_pessoa(id_pessoa: int) -> Pessoa:
    return await buscar_pessoa_por_id(id_pessoa)


async def atualizar_pessoa(id_pessoa: int, data: PessoaBase) -> Pessoa:
    pessoa = Pessoa(
        id=id_pessoa,
        nome=data.nome,
        idade=data.idade,
        moradia=data.moradia,
        area_util=data.area_util,
        experiencia_pets=data.experiencia_pets,
        tem_crianca=data.tem_crianca,
        outros_animais=data.outros_animais
    )

    await atualizar_pessoa(pessoa)
    return pessoa


async def remover_pessoa(id_pessoa: int) -> None:
    await deletar_pessoa(id_pessoa)
