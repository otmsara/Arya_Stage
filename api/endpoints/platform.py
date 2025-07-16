# Single endpoint file handling all platform operations from fastapi import APIRouter, HTTPException
from fastapi import APIRouter, HTTPException
from schemas.platform import BusinessIdeaResponse, UserProfile, ChatRequest, ChatResponse, BusinessPlanResponse
from api.core.agents.platform import platform

router = APIRouter()

@router.post("/profile", response_model=BusinessIdeaResponse)
async def set_user_profile(profile: UserProfile):
    """Set user profile and generate business ideas"""
    try:
        # Call the method on the platform instance
        message = platform.collect_user_profile(
            skills=profile.skills,
            interests=profile.interests,
            risk_tolerance=profile.risk_tolerance,
            budget=profile.budget,
            experience=profile.experience
        )
        ideas = platform.generate_business_ideas()
        return BusinessIdeaResponse(
            message=message,
            ideas=platform.generated_ideas
        )
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post("/select_idea/{idea_index}")
async def select_idea(idea_index: int):
    """Select a business idea and initialize agents"""
    try:
        message = platform.select_idea_and_build_team(idea_index)
        return {"message": message}
    except Exception as e:
        raise HTTPException(400, str(e))

@router.post("/chat/{agent_name}", response_model=ChatResponse)
async def chat_with_agent(agent_name: str, request: ChatRequest):
    """Chat with any agent"""
    agent = getattr(platform, f"{agent_name}_agent", None)
    if not agent:
        raise HTTPException(404, f"Agent {agent_name} not found")
    
    response = await getattr(platform, f"chat_with_{agent_name}")(
        message=request.message,
        history=request.history or []
    )
    
    return ChatResponse(
        agent_name=agent_name,
        response=response,
        business_context=platform.selected_idea
    )

@router.get("/business_plan", response_model=BusinessPlanResponse)
async def get_business_plan():
    """Generate comprehensive business plan"""
    if not platform.selected_idea:
        raise HTTPException(400, "No business idea selected")
    
    plan = platform.generate_business_plan()
    return BusinessPlanResponse(plan=plan)

@router.get("/export_data")
async def export_data():
    """Export all business data"""
    return platform.export_business_data()