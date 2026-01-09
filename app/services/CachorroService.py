from app.domain.CachorroModel import Cachorro
from app.schemas.CachorroSchema import CachorroCreate
from app.repositories.CachorroRepo import inserir_cachorro as repo_inserir_cachorro

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