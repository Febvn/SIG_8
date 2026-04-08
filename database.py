import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

class Database:
    def __init__(self):
        self.pool = None

    async def connect(self):
        if self.pool is None:
            self.pool = await asyncpg.create_pool(DATABASE_URL)
        return self.pool

    async def disconnect(self):
        if self.pool:
            await self.pool.close()

db = Database()

async def get_db():
    return await db.connect()
