# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    db_user: str
    db_password: str
    db_name: str
    db_host: str
    db_port: int
    fastapi_host: str
    fastapi_port: int
    log_level: str = "info"
    secret_key: str

    class Config:
        env_file = ".env"

settings = Settings()
