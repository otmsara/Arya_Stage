from pydantic import BaseModel
from typing import List, Dict, Optional

class UserProfile(BaseModel):
    skills: str
    interests: str
    risk_tolerance: str = "Moderate"
    budget: Optional[str] = None
    experience: str = "Beginner"

class BusinessIdea(BaseModel):
    name: str
    description: str
    target_customers: str
    revenue_model: str
    capital_required: str

class ChatMessage(BaseModel):
    content: str
    is_user: bool
    timestamp: str