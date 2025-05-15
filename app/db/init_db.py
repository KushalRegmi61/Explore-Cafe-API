# app/db/init_db.py
import asyncpg
from app.core.config import settings

CREATE_CAFE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS cafes (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT NOT NULL,
    has_wifi BOOLEAN DEFAULT FALSE,
    rating INTEGER CHECK (rating >= 0 AND rating <= 5)
);
"""

async def init_db():
    conn = await asyncpg.connect(
        user=settings.db_user,
        password=settings.db_password,
        database=settings.db_name,
        host=settings.db_host,
        port=settings.db_port
    )
    try:
        await conn.execute(CREATE_CAFE_TABLE_QUERY)
    finally:
        await conn.close()
