from app.core.database import get_pool
from app.domain.CachorroModel import Cachorro
from app.repositories.AnimalRepo import inserir_animal

async def repo_inserir_cachorro(data):
    
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


async def repo_pesquisar_cachorro_id(id_animal: int) -> Cachorro | None:

    pool = await get_pool()

    async with pool.acquire() as conn:

        async with conn.cursor() as cur:

            try:

                await cur.execute(
                    """
                    SELECT an.id, an.raca, an.nome, an.sexo, an.idade, an.porte, an.temperamento, an.status, cac.necessidade_passeio, cac.independencia
                    FROM animal AS an
                    JOIN cachorro AS cac
                    ON an.id = cac.id_animal
                    WHERE an.id = %s
                    """,
                    (
                        id_animal
                    )
                )

                dados_cachorro = await cur.fetchone()

                if not dados_cachorro:

                    return None
                
                return Cachorro(
                    id=dados_cachorro[0],
                    raca=dados_cachorro[1],
                    nome=dados_cachorro[2],
                    sexo=dados_cachorro[3],
                    idade=dados_cachorro[4],
                    porte=dados_cachorro[5],
                    temperamento=dados_cachorro[6],
                    status=dados_cachorro[7],
                    necessidade_passeio=dados_cachorro[8],
                    independencia=dados_cachorro[9]
                )
            
            except Exception:

                await conn.rollback()

                raise


async def repo_atualizar_cachorro(id_animal: int, data) -> None:

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

                campos_cachorro = []
                valores_cachorro = []

                for campo in ["necessidade_passeio", "independencia"]:
                    valor = getattr(data, campo)
                    if valor is not None:
                        campos_cachorro.append(f"{campo} = %s")
                        valores_cachorro.append(valor)

                if campos_cachorro:
                    await cur.execute(
                        f"""
                        UPDATE cachorro
                        SET {', '.join(campos_cachorro)}
                        WHERE id_animal = %s
                        """,
                        valores_cachorro + [id_animal]
                    )

                await conn.commit()

            except Exception:
                await conn.rollback()
                raise


async def repo_deletar_cachorro(id_animal: int) -> None:

    pool = await get_pool()

    async with pool.acquire() as conn:

        async with conn.cursor() as cur:

            try:

                await cur.execute(
                    """
                    DELETE FROM cachorro WHERE id_animal = %s
                    """,
                    (
                        id_animal
                    )
                )

                await cur.execute(
                    """
                    DELETE FROM animal WHERE id = %s
                    """,
                    (
                        id_animal
                    )
                )

                await conn.commit()
            
            except Exception:

                await conn.rollback()

                raise

