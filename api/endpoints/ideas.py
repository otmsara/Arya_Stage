from fastapi import APIRouter, Depends, HTTPException
from ..dependencies import get_platform
from ai_business_school.core.models import UserProfile

router = APIRouter()

@router.post("/generate")
async def generate_ideas(
    profile: UserProfile,
    platform = Depends(get_platform)
):
    """Generate business ideas based on user profile"""
    try:
        platform.user_profile = profile.dict()
        ideas = platform.agents['idea_scout'].generate_ideas(profile)
        return {"ideas": ideas}
    except Exception as e:
        raise HTTPException(500, f"Generation failed: {str(e)}")

@router.post("/select/{idea_id}")
async def select_idea(
    idea_id: int,
    platform = Depends(get_platform)
):
    """Select an idea for further analysis"""
    if not platform.generated_ideas:
        raise HTTPException(400, "Generate ideas first")
    
    try:
        platform.selected_idea = platform.generated_ideas[idea_id]
        return {"message": f"Selected: {platform.selected_idea['name']}"}
    except IndexError:
        raise HTTPException(404, "Idea not found")