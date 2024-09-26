import abc
import logging

from app.domain.integration_service import (
    IntegrationServiceTaskImportEntity,
    IntegrationServiceTaskEntity,
    IIntegrationServiceTaskRepository,
    IntegrationServiceTaskCreateEntity,
    IntegrationServiceTaskImportResponseEntity,
)

logger = logging.getLogger(__name__)


class ICreateIntegrationServiceTaskService(abc.ABC):
    def __init__(self, repository: IIntegrationServiceTaskRepository):
        self.repository = repository

    @abc.abstractmethod
    async def __call__(self, integration_service: IntegrationServiceTaskImportEntity) -> IntegrationServiceTaskEntity:
        pass


class CreateIntegrationServiceTaskService(ICreateIntegrationServiceTaskService):
    async def __call__(self, integration_service: IntegrationServiceTaskImportEntity) -> IntegrationServiceTaskImportResponseEntity:
        create_data = IntegrationServiceTaskCreateEntity(**integration_service.dict())
        integration_service_: IntegrationServiceTaskEntity = await self.repository.create(create_data)
        return IntegrationServiceTaskImportResponseEntity(id=integration_service_.id, task_id=integration_service.dict()["task_id"])
