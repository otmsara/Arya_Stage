# Main router
from fastapi import APIRouter
from api.endpoints.platform import router as platform_router

router = APIRouter()

# Single router for all platform operations
router.include_router(
    platform_router,
    prefix="/platform",
    tags=["Business Platform"]
)

# Health check
@router.get("/health")
async def health_check():
    return {"status": "healthy"}