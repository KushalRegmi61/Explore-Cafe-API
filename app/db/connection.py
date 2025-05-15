# app/db/connection.py
import asyncpg
from app.core.config import settings

async def get_connection():
    return await asyncpg.connect(
        user=settings.db_user,
        password=settings.db_password,
        database=settings.db_name,
        host=settings.db_host,
        port=settings.db_port
    )
