import threading
from app.kafka.importers import IntegrationServiceTaskImportService


kafka_thread = threading.Thread(target=IntegrationServiceTaskImportService.run)
kafka_thread.start()
