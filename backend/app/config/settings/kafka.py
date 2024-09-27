from os import getenv

from pydantic_settings import BaseSettings


class KafkaSettings(BaseSettings):
    """Настройки Кафки."""

    KAFKA_IMPORT_TOPIC: str = getenv("KAFKA_IMPORT_TOPIC", "KAFKA_IMPORT_TOPIC")
    KAFKA_RESULT_TOPIC: str = getenv("KAFKA_RESULT_TOPIC", "KAFKA_RESULT_TOPIC")

    class Config:
        """Конфиг."""

        env_prefix = "kafka_"