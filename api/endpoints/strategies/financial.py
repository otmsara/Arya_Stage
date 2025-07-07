from fastapi import APIRouter, Depends
from ...dependencies import get_platform, get_current_idea

router = APIRouter(prefix="/financial")

@router.get("/plan")
async def get_financial_plan(
    idea: dict = Depends(get_current_idea),
    platform = Depends(get_platform)
):
    """Get 3-year financial projections"""
    cfo = platform.agents['cfo']
    return {
        "financial_plan": cfo.generate_financial_plan(idea),
        "salary_benchmarks": cfo.context_data.get('research_data')
    }

@router.get("/funding-options")
async def get_funding_options(
    idea: dict = Depends(get_current_idea),
    platform = Depends(get_platform)
):
    """Get recommended funding strategies"""
    prompt = f"Suggest funding options for {idea['name']} with {idea.get('capital_required')} budget"
    return {"options": platform.agents['cfo'].get_response(prompt)}