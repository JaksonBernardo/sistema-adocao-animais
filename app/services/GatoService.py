from app.domain.GatoModel import Gato
from app.schemas.GatoSchema import GatoCreate
from app.repositories.GatoRepo import inserir_gato as repo_inserir_gato



# SERVICE DO GATO
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