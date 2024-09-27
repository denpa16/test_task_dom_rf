import json

import logging

from app.kafka.services import BaseKafkaService


logger = logging.getLogger(__name__)


class BaseExportService:
    """Сервис экспорта данных в Кафку."""

    def __init__(self) -> None:
        """Инициализация."""
        self.bootstrap_servers = 'kafka:9092'
        self.producer = self.get_producer()

    def get_producer(self) -> BaseKafkaService:
        """Получение."""
        service = BaseKafkaService(self.topic)
        return service._get_producer()

    def produce(self, message):
        self.producer.produce(self.topic, key=str(message["id"]), value=json.dumps(message))
        self.producer.flush()

    @property
    async def topic(self) -> str:
        """Топик."""
        raise NotImplementedError

