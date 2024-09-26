from __future__ import annotations

from os import getenv

from pydantic import PostgresDsn, ValidationInfo, field_validator
from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    """Настройки базы данных."""

    scheme: str = "postgresql+asyncpg"
    port: int = getenv("POSTGRES_PORT", "5432")
    host: str = getenv("POSTGRES_HOST", "db")
    user: str = getenv("POSTGRES_USER")
    password: str = getenv("POSTGRES_PASSWORD")
    db: str = getenv("POSTGRES_DB", "postgres")
    dsn: PostgresDsn | None | str = None
    echo: bool = True

    @field_validator("dsn", mode="before")
    @classmethod
    def dsn_build(cls: DatabaseSettings, value: str | None, values: ValidationInfo) -> str:
        """Создание dsn БД."""
        if isinstance(value, str):
            return value
        return PostgresDsn.build(
            scheme=values.data.get("scheme"),
            username=values.data.get("user"),
            password=values.data.get("password"),
            host=values.data.get("host"),
            port=values.data.get("port"),
            path=values.data.get("db"),
        ).unicode_string()

    class Config:
        """Конфиг."""

        env_prefix = "postgres_"
