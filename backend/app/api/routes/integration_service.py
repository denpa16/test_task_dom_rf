from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.resourses import async_session
from app.data.repositories import IntegrationServiceTaskRepository
from app.domain.integration_service import (
    IntegrationServiceTaskImportEntity,
    IntegrationServiceTaskEntity,
    IntegrationServiceTaskImportResponseEntity,
    IIntegrationServiceTaskRepository,
)
from app.domain.integration_service.services.create import CreateIntegrationServiceTaskService, ICreateIntegrationServiceTaskService

router = APIRouter(prefix="/integration_service", tags=["IntegrationService"])


@router.post(
    "/",
    #response_model=IntegrationServiceTaskImportResponseEntity
)
async def import_messages(
        integration_task: IntegrationServiceTaskImportEntity,
        session: AsyncSession = async_session
):
    """Импорт сообщений."""
    repo: IIntegrationServiceTaskRepository = IntegrationServiceTaskRepository(session)
    service: ICreateIntegrationServiceTaskService = CreateIntegrationServiceTaskService(repository=repo)
    integration_service: IntegrationServiceTaskImportResponseEntity = await service(integration_task)
    return integration_service