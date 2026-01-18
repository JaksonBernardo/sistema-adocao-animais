from app.core.database import get_pool
from app.domain.GatoModel import Gato
from app.repositories.AnimalRepo import inserir_animal


async def repo_pesquisar_gato_id(id_animal: int) -> Gato | None:

    pool = await get_pool()

    async with pool.acquire() as conn:

        async with conn.cursor() as cur:

            try:

                await cur.execute(
                    """
                    SELECT an.id, an.raca, an.nome, an.sexo, an.idade, an.porte, an.temperamento, an.status, gt.necessidade_passeio, gt.independencia
                    FROM animal AS an
                    JOIN gato AS gt
                    ON an.id = gt.id_animal
                    WHERE an.id = %s
                    """,
                    (
                        id_animal
                    )
                )

                dados_gato = await cur.fetchone()

                if not dados_gato:

                    return None
                
                return Gato(
                    id=dados_gato[0],
                    raca=dados_gato[1],
                    nome=dados_gato[2],
                    sexo=dados_gato[3],
                    idade=dados_gato[4],
                    porte=dados_gato[5],
                    temperamento=dados_gato[6],
                    status=dados_gato[7],
                    necessidade_passeio=dados_gato[8],
                    independencia=dados_gato[9]
                )
            
            except Exception:

                await conn.rollback()

                raise


async def repo_inserir_gato(data) -> int:

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


async def repo_atualizar_gato(id_animal: int, data) -> None:

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


async def repo_deletar_gato(id_animal: int) -> None:

    pool = await get_pool()

    async with pool.acquire() as conn:

        async with conn.cursor() as cur:

            try:

                await cur.execute(
                    """
                    DELETE FROM gato WHERE id_animal = %s
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


