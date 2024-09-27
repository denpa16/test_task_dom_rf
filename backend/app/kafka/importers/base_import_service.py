import logging

from confluent_kafka import Consumer, KafkaException

from app.kafka.services import BaseKafkaService

logger = logging.getLogger(__name__)


class BaseImporterService:
    """Сервис импорта данных."""


    def __init__(self) -> None:
        """Инициализация."""
        self.group = "group_id"
        self.consumer = self.get_consumer()

    def get_consumer(self) -> Consumer:
        """Получение."""
        service = BaseKafkaService(self.topic)
        return service._get_consumer()

    @property
    def topic(self) -> str:
        """Топик."""
        raise NotImplementedError

    def process_msg(self, _) -> None:
        raise NotImplementedError

    @classmethod
    def run(cls) -> None:
        """Запуск чтения."""
        self = cls()
        if self.consumer:
            while True:
                msg = self.consumer.poll(0.1)
                if msg is None:
                    continue
                if msg.error():
                    continue
                try:
                    self.process_msg(msg.value())
                except Exception as exc:
                    logging.error(str(exc))
