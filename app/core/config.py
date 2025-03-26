from pydantic import BaseSettings


class Settings(BaseSettings):
    # Variables de entorno
    DATABASE_URL: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"


settings = Settings()
