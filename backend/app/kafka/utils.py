from faststream.kafka import KafkaBroker, KafkaMessage

from app.config import settings

KAFKA_BOOTSTRAP_SERVERS = "kafka:9094"
kafka_broker = KafkaBroker(KAFKA_BOOTSTRAP_SERVERS)
TOPIC = "IntegrationServiceTaskExportTopic"

@kafka_broker.subscriber(TOPIC)
async def subscribe_message(message: KafkaMessage):
    print(f"Received message: {message._decoded_body}")

async def publish_message(message: str):
    await kafka_broker.publish(message, topic=TOPIC)
