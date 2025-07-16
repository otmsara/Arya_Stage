# Pydantic models for API
from pydantic import BaseModel
from typing import List, Dict, Optional

class UserProfile(BaseModel):
    skills: str
    interests: str
    risk_tolerance: str
    budget: str
    experience: str

class BusinessIdea(BaseModel):
    name: str
    description: str
    market_opportunity: str
    target_customers: str
    revenue_model: str
    capital_required: str
    time_to_market: str
    risk_level: str
    market_potential: int
    skills_match: int
    scalability: int
    innovation_score: int

class BusinessIdeaResponse(BaseModel):
    message: str
    ideas: List[BusinessIdea]

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[Dict]] = None

class ChatResponse(BaseModel):
    agent_name: str
    response: str
    business_context: Dict

class BusinessPlanResponse(BaseModel):
    plan: str