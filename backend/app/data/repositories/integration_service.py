from typing import Type

from pydantic import parse_obj_as
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import and_, bindparam, exc, select, update

from app.data.models import IntegrationServiceTask
from app.domain.integration_service import IntegrationServiceTaskCreateEntity, IntegrationServiceTaskEntity, IIntegrationServiceTaskRepository


class IntegrationServiceTaskRepository(IIntegrationServiceTaskRepository):
    def __init__(self, async_session: AsyncSession):
        self.session: AsyncSession = async_session
        self.model: Type[IntegrationServiceTask] = IntegrationServiceTask

    async def create(self, integration_service: IntegrationServiceTaskCreateEntity) -> IntegrationServiceTaskEntity:
        integration_service_ = self.model(**integration_service.dict())
        self.session.add(integration_service_)
        await self.session.flush()
        return parse_obj_as(IntegrationServiceTaskEntity, integration_service_)


    async def retrieve(self, id: int) -> IntegrationServiceTaskEntity | None:
        result = await self.session.execute(select(self.model).where(id=id))
        try:
            integration_service = result.scalars().one()
        except exc.NoResultFound:
            return None
        return parse_obj_as(IntegrationServiceTaskEntity, integration_service)
