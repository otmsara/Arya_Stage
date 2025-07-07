from .base_agent import AIAgent
from typing import Dict, List
import json

class IdeaScoutAgent(AIAgent):
    def __init__(self):
        super().__init__(
            name="Idea Scout",
            role="Business Idea Generator",
            expertise="trend spotting and opportunity identification"
        )
    
    def generate_ideas(self, user_profile: Dict) -> List[Dict]:
        """Generate personalized business ideas"""
        prompt = f"""
        Generate business ideas for:
        Skills: {user_profile.get('skills')}
        Interests: {user_profile.get('interests')}
        Risk Tolerance: {user_profile.get('risk_tolerance')}
        """
        
        response = self.get_response(
            prompt,
            "Return JSON array with 5 ideas following the exact schema"
        )
        
        try:
            # Clean response and parse JSON
            if response.startswith('```json'):
                response = response[7:-3]
            return json.loads(response)
        except json.JSONDecodeError:
            return self._get_fallback_ideas(user_profile)
    
    def _get_fallback_ideas(self, user_profile: Dict) -> List[Dict]:
        """Fallback ideas if JSON parsing fails"""
        return [
            {
                "name": "AI Productivity Tool",
                "description": "SaaS platform for automating workflows",
                "market_opportunity": "Growing remote work trend"
            }
            # ... additional fallback ideas
        ]