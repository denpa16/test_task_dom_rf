from faststream.kafka import KafkaBroker, KafkaMessage

from app.config import settings

KAFKA_BOOTSTRAP_SERVERS = settings.kafka.bootstrap_servers
kafka_broker = KafkaBroker(KAFKA_BOOTSTRAP_SERVERS)
