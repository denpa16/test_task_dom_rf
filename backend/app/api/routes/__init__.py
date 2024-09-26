from fastapi import APIRouter
from .integration_service import router as integration_service_router


api_router = APIRouter(prefix="/api")
api_router.include_router(integration_service_router)

