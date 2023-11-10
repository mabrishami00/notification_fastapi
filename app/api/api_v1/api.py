from fastapi import APIRouter
from .endpoints.notification import router as notification_router

router = APIRouter()
router.include_router(notification_router)
