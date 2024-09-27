from os import getenv

from pydantic_settings import BaseSettings


class KafkaSettings(BaseSettings):
    """Настройки Кафки."""

    import_topic: str = getenv("KAFKA_IMPORT_TOPIC", "KAFKA_IMPORT_TOPIC")
    result_topic: str = getenv("KAFKA_RESULT_TOPIC", "KAFKA_RESULT_TOPIC")
    bootstrap_servers: str = getenv("kafka:9094", "KAFKA_BOOTSTRAP_SERVERS")

    class Config:
        """Конфиг."""

        env_prefix = "kafka_"