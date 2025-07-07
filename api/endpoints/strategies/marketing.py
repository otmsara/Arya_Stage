from fastapi import APIRouter, Depends, HTTPException
from ...dependencies import get_platform, get_current_idea

router = APIRouter(prefix="/marketing")

@router.get("/plan")
async def get_marketing_plan(
    idea: dict = Depends(get_current_idea),
    platform = Depends(get_platform)
):
    """Get comprehensive marketing strategy"""
    try:
        cmo = platform.agents['cmo']
        plan = cmo.generate_marketing_plan(idea)
        return {
            "plan": plan,
            "research_data": cmo.context_data.get('research_data')
        }
    except Exception as e:
        raise HTTPException(500, f"Marketing plan generation failed: {str(e)}")

@router.get("/channels")
async def get_recommended_channels(
    idea: dict = Depends(get_current_idea),
    platform = Depends(get_platform)
):
    """Get recommended marketing channels"""
    prompt = f"Based on this business: {idea['name']}, list top 5 marketing channels"
    response = platform.agents['cmo'].get_response(prompt)
    return {"channels": response.split("\n")}