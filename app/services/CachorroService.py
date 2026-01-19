from app.domain.CachorroModel import Cachorro
from app.schemas.CachorroSchema import CachorroCreate, CachorroUpdate
from app.repositories.CachorroRepo import repo_inserir_cachorro, repo_atualizar_cachorro, repo_deletar_cachorro, repo_pesquisar_cachorro_id


async def inserir_cachorro(animal_data: CachorroCreate) -> Cachorro:

    cachorro = Cachorro(
        id = 0,
        raca = animal_data.raca,
        nome = animal_data.nome,
        sexo = animal_data.sexo,
        idade = animal_data.idade,
        porte = animal_data.porte,
        temperamento = animal_data.temperamento,
        status = animal_data.status,
        necessidade_passeio = animal_data.necessidade_passeio,
        independencia = animal_data.independencia
    )

    id_cachorro = await repo_inserir_cachorro(animal_data)

    cachorro.id = id_cachorro

    return cachorro

async def ler_cachorro(id_animal: int) -> Cachorro | None:

    cachorro = await repo_pesquisar_cachorro_id(id_animal)

    if not cachorro:

        raise ValueError("Animal não encontrado")

    return cachorro

async def atualizar_cachorro(id_animal: int, animal_data: CachorroUpdate) -> Cachorro:

    await repo_atualizar_cachorro(id_animal, animal_data)

    return Cachorro(
        id=id_animal,
        raca=animal_data.raca,
        nome=animal_data.nome,
        sexo=animal_data.sexo,
        idade=animal_data.idade,
        porte=animal_data.porte,
        temperamento=animal_data.temperamento,
        status=animal_data.status,
        necessidade_passeio=animal_data.necessidade_passeio,
        independencia=animal_data.independencia
    )

async def deletar_cachorro(id_animal: int) -> None:

    gato = await repo_pesquisar_cachorro_id(id_animal)

    if not gato:

        raise ValueError("Animal não encontrado")
    
    if gato.status == "ADOTADO":

        raise ValueError("Este animal não pode ser deletado pois seu status = ADOTADO")
    
    await repo_deletar_cachorro(id_animal)

