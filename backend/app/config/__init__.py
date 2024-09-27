from pydantic_settings import BaseSettings

from .settings import (
    AppSettings,
    DatabaseSettings,
    KafkaSettings,
)


class Settings(BaseSettings):
    """Настройки."""

    database: DatabaseSettings = DatabaseSettings()
    app: AppSettings = AppSettings()
    kafka: KafkaSettings = KafkaSettings()


settings = Settings()
