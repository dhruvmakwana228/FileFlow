from fastapi import FastAPI

app = FastAPI(
    title = "FileFlow",
    description = "Smart Large Folder Upload & Transfer System",
    version = "1.0.0"
)

@app.get("/")
def home():
    return{
        "message": "Welcome to FileFlow",
        "status": "running"
    }

@app.get("/health")
def health_check():
    return{
        "status": "healthy"
    }