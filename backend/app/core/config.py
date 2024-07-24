from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()


class Settings(BaseSettings):
    # Configuración de la base de datos
    DATABASE_URL: str = os.getenv("DATABASE_URL")

    # Configuración de seguridad
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    # Configuración de CORS (si es necesario)
    BACKEND_CORS_ORIGINS: list = os.getenv("BACKEND_CORS_ORIGINS").split(",")


settings = Settings()
