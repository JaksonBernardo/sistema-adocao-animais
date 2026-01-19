from app.domain.AdotanteModel import Adotante
from app.schemas.AdotanteSchema import AdotanteCreate, AdotanteUpdate
from app.repositories.AdotanteRepo import inserir_adotante, buscar_adotante_por_id, atualizar_adotante, deletar_adotante

async def criar_adotante(data: AdotanteCreate) -> Adotante:

    adotante = Adotante(
        id=0,
        nome=data.nome,
        idade=data.idade,
        moradia=data.moradia,
        area_util=data.area_util,
        experiencia_pets=data.experiencia_pets,
        tem_crianca=data.tem_crianca,
        outros_animais=data.outros_animais,
        renda_mensal=data.renda_mensal
    )

    adotante_id = await inserir_adotante(adotante)
    adotante._id = adotante_id

    return adotante


async def obter_adotante(id_pessoa: int) -> Adotante:
    return await buscar_adotante_por_id(id_pessoa)


async def atualizar_adotante(id_pessoa: int, data: AdotanteUpdate) -> Adotante:
    adotante = Adotante(
        id=id_pessoa,
        nome=data.nome,
        idade=data.idade,
        moradia=data.moradia,
        area_util=data.area_util,
        experiencia_pets=data.experiencia_pets,
        tem_crianca=data.tem_crianca,
        outros_animais=data.outros_animais,
        renda_mensal=data.renda_mensal
    )

    await atualizar_adotante(adotante)
    return adotante


async def remover_adotante(id_pessoa: int) -> None:
    await deletar_adotante(id_pessoa)
