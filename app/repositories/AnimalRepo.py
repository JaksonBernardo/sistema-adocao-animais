
async def inserir_animal(cur, data):
    await cur.execute(
        """
        INSERT INTO animal
        (raca, nome, sexo, idade, porte, temperamento, status)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            data.raca,
            data.nome,
            data.sexo,
            data.idade,
            data.porte,
            data.temperamento,
            data.status
        )
    )

    return cur.lastrowid



