from fastapi import APIRouter

router = APIRouter(prefix="/api/uploads", tags=["uploads"],)

@router.get("/health")
def upload_health():
    return {
        "status": "healthy",
        "module": "uploads",
        "message": "FileFlow upload API is ready",
    }