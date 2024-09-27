from .base_import_service import BaseImporterService
from sqlalchemy.ext.asyncio import AsyncSession

from app.data.repositories import IntegrationServiceTaskRepository
from app.domain.integration_service import (
    IntegrationServiceTaskImportEntity,
    IntegrationServiceTaskEntity,
    IntegrationServiceTaskImportResponseEntity,
    IIntegrationServiceTaskRepository,
)
from app.domain.integration_service.services.create import CreateIntegrationServiceTaskService, ICreateIntegrationServiceTaskService
from app.dependencies.resourses import async_session
from app.data.models import IntegrationServiceTask


class IntegrationServiceTaskImportService(BaseImporterService):
    """Импортер задач интеграционного сервиса."""

    topic = "IntegrationServiceTaskExportTopic"

    def process_msg(self, msg: dict) -> None:
        print("$$$$$")
        print(msg)
        print("$$$$$")
        #session: AsyncSession = async_session
        #integration_task = IntegrationServiceTask(**msg)
        #repo: IIntegrationServiceTaskRepository = IntegrationServiceTaskRepository(session)
        #service: ICreateIntegrationServiceTaskService = CreateIntegrationServiceTaskService(repository=repo)
        #await service(integration_task)

