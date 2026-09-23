from fastapi import APIRouter

from app.core.logger import logger

router = APIRouter()

@router.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello World"}
