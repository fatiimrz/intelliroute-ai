from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.core.config import get_settings

app = FastAPI(title=get_settings().app_name, version="0.1.0")
app.include_router(health_router, prefix="/api/v1")
