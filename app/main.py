from fastapi import FastAPI
from app.api.endpoints import cafes  # <-- import the cafes router module
from app.db.init_db import init_db


app = FastAPI()

# Register the cafes router under a prefix
app.include_router(cafes.router, prefix="/cafes", tags=["cafes"])

# method to start on startup 
@app.on_event("startup")
async def on_startup():
    await init_db()