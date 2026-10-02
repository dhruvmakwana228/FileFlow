from fastapi import FastAPI

from app.core.config import settings

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