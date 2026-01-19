from app.core.database import get_pool
from app.domain.PessoaModel import Pessoa


async def inserir_pessoa(pessoa: Pessoa) -> int:
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
                        pessoa.nome,
                        pessoa.idade,
                        pessoa.moradia,
                        pessoa.area_util,
                        pessoa.experiencia_pets,
                        pessoa.tem_crianca,
                        pessoa.outros_animais
                    )
                )

                pessoa_id = cur.lastrowid
                await conn.commit()
                return pessoa_id

            except Exception:
                await conn.rollback()
                raise


async def buscar_pessoa_por_id(id_pessoa: int) -> Pessoa | None:
    pool = await get_pool()

    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                """
                SELECT id, nome, idade, moradia, area_util, experiencia_pets,
                       tem_crianca, outros_animais
                FROM pessoa
                WHERE id = %s
                """,
                (id_pessoa,)
            )

            row = await cur.fetchone()

            if not row:
                return None

            return Pessoa(*row)


async def atualizar_pessoa(pessoa: Pessoa) -> None:
    pool = await get_pool()

    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await conn.execute(
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
                    pessoa.nome,
                    pessoa.idade,
                    pessoa.moradia,
                    pessoa.area_util,
                    pessoa.experiencia_pets,
                    pessoa.tem_crianca,
                    pessoa.outros_animais,
                    pessoa.id
                )
            )


async def deletar_pessoa(id_pessoa: int) -> None:
    pool = await get_pool()

    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute(
                "DELETE FROM pessoa WHERE id = %s",
                (id_pessoa,)
            )
