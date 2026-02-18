from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USER: str = Field(description="Пользователь", default="postgres", examples=["postgres"])
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def URI_ALEMBIC(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
