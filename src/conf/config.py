from pydantic import Field
from pydantic_settings import BaseSettings


class Setting(BaseSettings):
    DB_USER: str = Field(description="Пользователь", default="postgres", examples=["postgres"])
    DB_PASS: str = Field(description="Пароль", default="postgres", examples=["postgres"])
    DB_HOST: str = Field(description="Хост", default="localhost", examples=["localhost"])
    DB_PORT: str = Field(description="Порт", default="5433", examples=["5433"])
    DB_NAME: str = Field(description="Имя БД", default="tms_db", examples=["tms_db"])

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def URI_ALEMBIC(self) -> str:
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Setting()
