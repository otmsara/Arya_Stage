from fastapi import APIRouter, Depends
from ...dependencies import get_platform, get_current_idea

router = APIRouter(prefix="/technical")

@router.get("/plan")
async def get_technical_plan(
    idea: dict = Depends(get_current_idea),
    platform = Depends(get_platform)
):
    """Get technical implementation plan"""
    return {
        "plan": platform.agents['cto'].generate_tech_plan(idea),
        "research": platform.agents['cto'].context_data.get('research_data')
    }