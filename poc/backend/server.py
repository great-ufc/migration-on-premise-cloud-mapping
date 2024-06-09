import uvicorn

from src.config import settings

if __name__ == "__main__":
    uvicorn.run(
        "src.app:app", 
        host=settings.API_HOST, 
        port=settings.API_PORT, 
        reload=True
    )