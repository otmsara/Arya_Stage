from fastapi import APIRouter, Depends
from ...dependencies import get_platform, get_current_idea

router = APIRouter(prefix="/hr")

@router.get("/plan")
async def get_hr_plan(
    idea: dict = Depends(get_current_idea),
    platform = Depends(get_platform)
):
    """Get people and culture strategy"""
    hr = platform.agents['hr']
    return {
        "hr_plan": hr.generate_hr_plan(idea),
        "talent_data": hr.context_data.get('research_data')
    }

@router.get("/hiring-roadmap")
async def get_hiring_roadmap(
    idea: dict = Depends(get_current_idea),
    platform = Depends(get_platform)
):
    """Get prioritized hiring plan"""
    prompt = f"Create 12-month hiring roadmap for {idea['name']}"
    return {"roadmap": platform.agents['hr'].get_response(prompt)}