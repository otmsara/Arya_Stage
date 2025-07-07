from fastapi import APIRouter, Depends
from ...dependencies import get_platform, get_current_idea

router = APIRouter(prefix="/legal")

@router.get("/plan")
async def get_legal_plan(
    idea: dict = Depends(get_current_idea),
    platform = Depends(get_platform)
):
    """Get legal framework recommendations"""
    legal = platform.agents['legal']
    return {
        "legal_plan": legal.generate_legal_plan(idea),
        "compliance_data": legal.context_data.get('research_data')
    }

@router.get("/entity-types")
async def get_entity_types(
    idea: dict = Depends(get_current_idea),
    platform = Depends(get_platform)
):
    """Get business entity type recommendations"""
    prompt = f"Recommend business entity types for {idea['name']} in the {idea.get('industry', 'tech')} sector"
    return {"entity_types": platform.agents['legal'].get_response(prompt)}