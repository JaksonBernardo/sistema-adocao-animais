from app.core.database import get_pool
from app.repositories.AnimalRepo import inserir_animal

async def repo_inserir_gato(data):

    pool = await get_pool()

    async with pool.acquire() as conn:

        async with conn.cursor() as cur:

            try:

                await conn.begin()

                animal_id = await inserir_animal(cur, data)

                await cur.execute(
                    """
                    INSERT INTO gato
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


async def repo_atualizar_gato(id_animal: int, data):

    pool = await get_pool()

    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            try:
                await conn.begin()

                campos = []
                valores = []

                for campo in [
                    "raca", "nome", "sexo", "idade",
                    "porte", "temperamento", "status"
                ]:
                    valor = getattr(data, campo)
                    if valor is not None:
                        campos.append(f"{campo} = %s")
                        valores.append(valor)

                if campos:
                    await cur.execute(
                        f"""
                        UPDATE animal
                        SET {', '.join(campos)}
                        WHERE id = %s
                        """,
                        valores + [id_animal]
                    )

                campos_gato = []
                valores_gato = []

                for campo in ["necessidade_passeio", "independencia"]:
                    valor = getattr(data, campo)
                    if valor is not None:
                        campos_gato.append(f"{campo} = %s")
                        valores_gato.append(valor)

                if campos_gato:
                    await cur.execute(
                        f"""
                        UPDATE gato
                        SET {', '.join(campos_gato)}
                        WHERE id_animal = %s
                        """,
                        valores_gato + [id_animal]
                    )

                await conn.commit()

            except Exception:
                await conn.rollback()
                raise

