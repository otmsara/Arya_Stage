from fastapi import APIRouter, Depends
from ...dependencies import get_platform, get_current_idea

router = APIRouter(prefix="/market")

@router.get("/analysis")
async def get_market_analysis(
    idea: dict = Depends(get_current_idea),
    platform = Depends(get_platform)
):
    """Get competitive market analysis"""
    market = platform.agents['market']
    return {
        "market_analysis": market.generate_market_analysis(idea),
        "competitor_data": market.context_data.get('research_data')
    }

@router.get("/competitors")
async def get_competitor_analysis(
    idea: dict = Depends(get_current_idea),
    platform = Depends(get_platform)
):
    """Get detailed competitor breakdown"""
    prompt = f"Analyze direct competitors for {idea['name']} in {idea.get('target_market')}"
    return {"competitors": platform.agents['market'].get_response(prompt)}