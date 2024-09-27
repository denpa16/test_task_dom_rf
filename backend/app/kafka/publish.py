from app.config import settings

from app.kafka.broker import kafka_broker


RESULT_TOPIC = settings.kafka.result_topic
IMPORT_TOPIC = settings.kafka.import_topic


async def publish_message_to_kafka(message: str):
    await kafka_broker.publish(message, topic=RESULT_TOPIC)
