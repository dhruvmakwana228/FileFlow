from fastapi import FastAPI
from sqlalchemy import text

from app.core.config import settings
from app.database.connection import engine

app = FastAPI(
    title = settings.APP_NAME,
    description = "Smart Large Folder Upload & Transfer System",
    version = settings.APP_VERSION
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