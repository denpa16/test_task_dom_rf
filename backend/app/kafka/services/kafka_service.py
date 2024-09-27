import logging

from confluent_kafka import Consumer, KafkaException, Producer

logger = logging.getLogger(__name__)


class BaseKafkaService:
    """Сервис Кафки."""

    def __init__(self, topic: str) -> None:
        """Инициализация."""
        self.topic = topic

    def _get_consumer(self):
        try:
            consumer = Consumer({
                'bootstrap.servers': 'kafka:9094',
                'group.id': 'mygroup',
                'auto.offset.reset': 'earliest'
            })
            consumer.subscribe([self.topic])
            return consumer
        except Exception:
            return None

    def _get_producer(self):
        try:
            return Producer({'bootstrap.servers': 'kafka:9094'})
        except Exception:
            return None
