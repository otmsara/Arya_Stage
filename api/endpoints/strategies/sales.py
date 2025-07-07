from fastapi import APIRouter, Depends
from ...dependencies import get_platform, get_current_idea

router = APIRouter(prefix="/sales")

@router.get("/plan")
async def get_sales_plan(
    idea: dict = Depends(get_current_idea),
    platform = Depends(get_platform)
):
    """Get revenue generation strategy"""
    sales = platform.agents['sales']
    return {
        "sales_plan": sales.generate_sales_plan(idea),
        "market_data": sales.context_data.get('research_data')
    }

@router.get("/pricing-strategy")
async def get_pricing_strategy(
    idea: dict = Depends(get_current_idea),
    platform = Depends(get_platform)
):
    """Get recommended pricing model"""
    prompt = f"Suggest pricing strategy for {idea['name']} with {idea.get('revenue_model')} model"
    return {"pricing": platform.agents['sales'].get_response(prompt)}