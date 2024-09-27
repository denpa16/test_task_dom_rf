from fastapi import FastAPI

from app.api import routes
from app.kafka.utils import kafka_broker

app = FastAPI()
app.include_router(router=routes.api_router)

@app.on_event("startup")
async def startup_event():
    await kafka_broker.start()

@app.on_event("shutdown")
async def shutdown_event():
    await kafka_broker.stop()

@app.get("/")
async def read_root():
    return {"Hello": "World"}