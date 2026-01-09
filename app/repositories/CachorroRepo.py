from app.core.database import get_pool
from app.repositories.AnimalRepo import inserir_animal

async def inserir_cachorro(data):
    
    pool = await get_pool()

    async with pool.acquire() as conn:

        async with conn.cursor() as cur:

            try:
                await conn.begin()

                animal_id = await inserir_animal(cur, data)

                await cur.execute(
                    """
                    INSERT INTO cachorro
                    (id_animal, necessidade_passeio, independencia)
                    VALUES (%s,%s,%s)
                    """,
                    (
                        animal_id,
                        data.necessidade_passeio,
                        data.independencia
                    )
                )

                await conn.commit()
                return animal_id

            except Exception:

                await conn.rollback()
                raise
