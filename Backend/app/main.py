from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from app.core.config import settings
from app.database.connection import Base, engine
from app.models import(User, Folder, File, Upload, UploadChunk)

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)

    yield

app = FastAPI(
    title = settings.APP_NAME,
    description = "Smart Large Folder Upload & Transfer System",
    version = settings.APP_VERSION,
    lifespan = lifespan
)

@app.get("/")
def home():
    return{
        "message": f"Welcome to {settings.APP_NAME}",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return{
        "status": "healthy"
    }

@app.get("/health/database")
def database_health_check():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception as error:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(error)
        }