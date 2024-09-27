import abc
import logging
import json

from app.domain.integration_service import (
    IntegrationServiceTaskImportEntity,
    IntegrationServiceTaskEntity,
    IIntegrationServiceTaskRepository,
    IntegrationServiceTaskCreateEntity,
    IntegrationServiceTaskImportResponseEntity,
)
from app.kafka.publish import publish_message_to_kafka
from app.data.models import TaskType
from app.external_data_services.dadata import request_dadata
from app.external_data_services.yandex_gpt import request_yandex_gpt

logger = logging.getLogger(__name__)


class ICreateIntegrationServiceTaskService(abc.ABC):
    def __init__(self, repository: IIntegrationServiceTaskRepository):
        self.repository = repository

    @abc.abstractmethod
    async def __call__(self, integration_service: IntegrationServiceTaskImportEntity) -> IntegrationServiceTaskEntity:
        pass


class CreateIntegrationServiceTaskService(ICreateIntegrationServiceTaskService):
    async def __call__(self, integration_service: IntegrationServiceTaskImportEntity) -> IntegrationServiceTaskImportResponseEntity:
        external_service_data = self._request_data_in_external_service(integration_service.dict())
        create_data = IntegrationServiceTaskCreateEntity(**external_service_data)
        integration_service_: IntegrationServiceTaskEntity = await self.repository.create(create_data)
        data = {"id": integration_service_.id, "task_id": integration_service.dict()["task_id"]}
        await publish_message_to_kafka(json.dumps(data))
        return IntegrationServiceTaskImportResponseEntity(**data)

    def _request_data_in_external_service(self, data) -> dict:
        if data["task_type"] in [TaskType.EMAIL, TaskType.PHONE]:
            return request_dadata(data)
        if data["task_type"] in [TaskType.GPT]:
            return request_yandex_gpt(data)
        return {}

