from sqlalchemy import Column, Integer, String, Enum
import enum

from app.data.models import Base

class TaskType(enum.Enum):
    """Тип задачи."""
    PHONE = "phone"
    EMAIL = "email"
    GPT = "gpt"


class IntegrationServiceTask(Base):
    """Задача интеграционного сервиса."""
    __tablename__ = "integration_service"

    id = Column(Integer, primary_key=True, autoincrement=True)
    data = Column(String, nullable=False)
    task_type = Column(Enum(TaskType), nullable=False)