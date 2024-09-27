from faststream.kafka import KafkaBroker, KafkaMessage
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.data.repositories import IntegrationServiceTaskRepository
from app.dependencies.resourses import async_session
from app.domain.integration_service import (
    IntegrationServiceTaskImportEntity,
    IntegrationServiceTaskEntity,
    IntegrationServiceTaskImportResponseEntity,
    IIntegrationServiceTaskRepository,
)
from app.domain.integration_service.services.create import CreateIntegrationServiceTaskService, ICreateIntegrationServiceTaskService
from app.kafka.broker import kafka_broker

IMPORT_TOPIC = settings.kafka.import_topic

@kafka_broker.subscriber(IMPORT_TOPIC)
async def subscribe_message_from_kafka(
        message: KafkaMessage,
        session: AsyncSession = async_session
):
    repo: IIntegrationServiceTaskRepository = IntegrationServiceTaskRepository(session)
    service: ICreateIntegrationServiceTaskService = CreateIntegrationServiceTaskService(repository=repo)
    await service(message)

