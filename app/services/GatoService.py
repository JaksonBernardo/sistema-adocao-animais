from app.domain.GatoModel import Gato
from app.schemas.GatoSchema import GatoCreate, GatoUpdate
from app.repositories.GatoRepo import repo_inserir_gato, repo_atualizar_gato, repo_pesquisar_gato_id, repo_deletar_gato


async def ler_gato(id_animal: int) -> Gato | None:

    gato = await repo_pesquisar_gato_id(id_animal)

    if not gato:

        raise ValueError("Animal não encontrado")

    return gato

async def inserir_gato(animal_data: GatoCreate) -> Gato:

    gato = Gato(
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

    id_gato = await repo_inserir_gato(animal_data)

    gato.id = id_gato

    return gato

async def atualizar_gato(id_animal: int, animal_data: GatoUpdate) -> Gato:

    await repo_atualizar_gato(id_animal, animal_data)

    return Gato(
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

async def deletar_gato(id_animal: int) -> None:

    gato = await repo_pesquisar_gato_id(id_animal)

    if not gato:

        raise ValueError("Animal não encontrado")
    
    if gato.status == "ADOTADO":

        raise ValueError("Este animal não pode ser deletado pois seu status = ADOTADO")
    
    await repo_deletar_gato(id_animal)




