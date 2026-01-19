# app/repositories/AdotanteRepo.py

from app.core.database import get_pool
from app.domain.AdotanteModel import Adotante


async def inserir_adotante(adotante: Adotante) -> int:
    pool = await get_pool()

    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await conn.begin()

            try:

                await cur.execute(
                    """
                    INSERT INTO pessoa 
                    (nome, idade, moradia, area_util, experiencia_pets, tem_crianca, outros_animais)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        adotante.nome,
                        adotante.idade,
                        adotante.moradia,
                        adotante.area_util,
                        adotante.experiencia_pets,
                        adotante.tem_crianca,
                        adotante.outros_animais
                    )
                )

                pessoa_id = cur.lastrowid

                await cur.execute(
                    """
                    INSERT INTO adotante (id_pessoa, renda_mensal)
                    VALUES (%s, %s)
                    """,
                    (
                        pessoa_id,
                        adotante.renda_mensal
                    )
                )

                await conn.commit()
                return pessoa_id

            except Exception:
                await conn.rollback()
                raise


async def buscar_adotante_por_id(id_pessoa: int) -> Adotante | None:
    pool = await get_pool()

    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                """
                SELECT p.id, p.nome, p.idade, p.moradia, p.area_util,
                       p.experiencia_pets, p.tem_crianca, p.outros_animais,
                       a.renda_mensal
                FROM pessoa p
                JOIN adotante a ON a.id_pessoa = p.id
                WHERE p.id = %s
                """,
                (id_pessoa,)
            )

            row = await cur.fetchone()

            if not row:
                return None

            return Adotante(*row)


async def atualizar_adotante(adotante: Adotante) -> None:
    pool = await get_pool()

    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await conn.begin()

            try:

                await cur.execute(
                    """
                    UPDATE pessoa SET
                        nome = %s,
                        idade = %s,
                        moradia = %s,
                        area_util = %s,
                        experiencia_pets = %s,
                        tem_crianca = %s,
                        outros_animais = %s
                    WHERE id = %s
                    """,
                    (
                        adotante.nome,
                        adotante.idade,
                        adotante.moradia,
                        adotante.area_util,
                        adotante.experiencia_pets,
                        adotante.tem_crianca,
                        adotante.outros_animais,
                        adotante.id
                    )
                )

                await cur.execute(
                    """
                    UPDATE adotante SET
                        renda_mensal = %s
                    WHERE id_pessoa = %s
                    """,
                    (
                        adotante.renda_mensal,
                        adotante.id
                    )
                )

                await conn.commit()

            except Exception:
                await conn.rollback()
                raise


async def deletar_adotante(id_pessoa: int) -> None:
    pool = await get_pool()

    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await conn.begin()

            try:
                await cur.execute(
                    "DELETE FROM adotante WHERE id_pessoa = %s",
                    (id_pessoa,)
                )

                await cur.execute(
                    "DELETE FROM pessoa WHERE id = %s",
                    (id_pessoa,)
                )

                await conn.commit()

            except Exception:
                await conn.rollback()
                raise
