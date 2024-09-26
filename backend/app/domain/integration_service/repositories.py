import abc

from app.domain.integration_service.entities import IntegrationServiceTaskCreateEntity, IntegrationServiceTaskEntity


class IIntegrationServiceTaskRepository(abc.ABC):

    @abc.abstractmethod
    async def create(self, user: IntegrationServiceTaskCreateEntity) -> IntegrationServiceTaskEntity:
        pass

    @abc.abstractmethod
    async def retrieve(self, id: int) -> IntegrationServiceTaskEntity:
        pass
