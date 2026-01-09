import aiomysql
from app.config import Config

_pool = None

async def get_pool():

    global _pool

    if _pool is None:

        _pool = await aiomysql.create_pool(
            host = Config.DB_HOST,
            port = Config.DB_PORT,
            user = Config.DB_USER,
            password = Config.DB_PASSWORD,
            db = Config.DB_NAME,
            minsize = 1,
            maxsize = 5,
            autocommit = True
        )

    return _pool
