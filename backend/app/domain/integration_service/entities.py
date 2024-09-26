from pydantic import BaseModel, EmailStr, Field, validator

from app.data.models import TaskType


class IntegrationServiceTaskImportEntity(BaseModel):
    task_id: int
    task_type: TaskType
    data: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "task_id": 123,
                    "task_type": TaskType.EMAIL,
                    "data": "example data"
                }
            ]
        }
    }

class IntegrationServiceTaskImportResponseEntity(BaseModel):
    id: int
    task_id: int

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": "1",
                    "task_id": "2"
                }
            ]
        }
    }

class IntegrationServiceTaskCreateEntity(BaseModel):
    task_type: TaskType
    data: str

    model_config = {
        "from_attributes":True
    }


class IntegrationServiceTaskEntity(BaseModel):
    id: int

    model_config = {
        "from_attributes":True
    }
