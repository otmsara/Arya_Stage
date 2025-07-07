from fastapi import Depends
from ai_business_school.core.platform import BusinessSchoolPlatform
from ai_business_school.config import Config

def get_platform():
    platform = BusinessSchoolPlatform()
    # Configure all agents
    for agent in platform.agents.values():
        agent.configure_openai(
            Config.OPENAI_API_KEY,
            Config.OPENAI_API_BASE,
            Config.OPENAI_API_VERSION
        )
    return platform

def get_current_idea(platform: BusinessSchoolPlatform = Depends(get_platform)):
    if not platform.selected_idea:
        raise HTTPException(400, "No business idea selected")
    return platform.selected_idea