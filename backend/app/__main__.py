from fastapi import FastAPI

from app.api import routes

import threading
from app.kafka.importers import IntegrationServiceTaskImportService

app = FastAPI()
app.include_router(router=routes.api_router)


kafka_thread = threading.Thread(target=IntegrationServiceTaskImportService.run)
kafka_thread.start()
