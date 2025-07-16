from .base import AIAgent
from typing import Dict, List
from datetime import datetime
import json

class IdeaScoutAgent(AIAgent):
    def __init__(self):
        super().__init__("Idea Scout", "Business Idea Generator", "trend spotting, market opportunity identification, and entrepreneurial strategy")

    def generate_ideas(self, user_profile: Dict) -> List[Dict]:
        current_year = datetime.now().year

        prompt = f"""
        You are an expert business strategist and trend analyst. Based on the user profile below, generate 5 highly tailored, innovative business ideas that leverage current market trends and emerging opportunities in {current_year}.

        USER PROFILE:
        - Skills & Expertise: {user_profile.get('skills', 'Not specified')}
        - Interests & Passions: {user_profile.get('interests', 'Not specified')}
        - Risk Tolerance: {user_profile.get('risk_tolerance', 'Moderate')}
        - Available Budget: {user_profile.get('budget', 'Not specified')}
        - Business Experience: {user_profile.get('experience', 'Not specified')}

        REQUIREMENTS:
        1. Each idea should leverage current market trends (AI/ML, sustainability, remote work, digital transformation, etc.)
        2. Ideas must align with the user's skills and interests
        3. Consider budget constraints and risk tolerance
        4. Focus on scalable, technology-enabled business models
        5. Include specific market opportunities and competitive advantages

        For each business idea, provide detailed analysis in this EXACT JSON format:
        {{
            "name": "Creative, memorable business name",
            "tagline": "Compelling one-line value proposition",
            "description": "Detailed 2-3 sentence description of the business concept",
            "market_opportunity": "Specific market gap or trend this addresses",
            "target_customers": "Primary customer segments",
            "revenue_model": "How the business makes money",
            "competitive_advantage": "Key differentiators from competitors",
            "market_potential": [1-10 score],
            "skills_match": [1-10 score based on user skills],
            "risk_level": "Low/Medium/High with brief explanation",
            "capital_required": "Specific dollar range",
            "time_to_market": "Estimated months from concept to launch",
            "scalability": "1-10 score for growth potential",
            "innovation_score": "1-10 for uniqueness/disruption potential"
        }}

        Return ONLY a valid JSON array of 5 business ideas. No additional text or explanation.
        """

        try:
            response = self.get_response(prompt, "Focus on creating innovative, data-driven business concepts that align perfectly with the user's profile. Ensure all JSON is properly formatted.")

            cleaned_response = response.strip()
            if cleaned_response.startswith('```json'):
                cleaned_response = cleaned_response[7:-3]
            elif cleaned_response.startswith('```'):
                cleaned_response = cleaned_response[3:-3]

            ideas = json.loads(cleaned_response)

            if isinstance(ideas, list) and len(ideas) > 0:
                return ideas
            else:
                raise ValueError("Invalid JSON structure")

        except Exception as e:
            print(f"Error parsing AI response: {e}")
            return self._get_fallback_ideas(user_profile)

    def _get_fallback_ideas(self, user_profile: Dict) -> List[Dict]:
        """Enhanced fallback ideas with more detail"""
        skills = user_profile.get('skills', '').lower()
        interests = user_profile.get('interests', '').lower()
        risk_tolerance = user_profile.get('risk_tolerance', 'Moderate')

        ideas = [
            {
                "name": "AI-Powered Workflow Optimizer",
                "tagline": "Automate repetitive tasks with intelligent AI agents",
                "description": "SaaS platform that uses AI to identify and automate repetitive business processes across different industries, saving companies 40-60% on operational costs.",
                "market_opportunity": "Growing demand for business process automation post-pandemic",
                "target_customers": "Small to medium businesses, remote teams, consultants",
                "revenue_model": "Monthly SaaS subscriptions ($49-$299/month)",
                "competitive_advantage": "Industry-agnostic AI that learns from user behavior",
                "market_potential": 9,
                "skills_match": 8 if 'programming' in skills or 'ai' in skills else 6,
                "risk_level": "Medium - High demand but competitive market",
                "capital_required": "$25,000 - $75,000",
                "time_to_market": "4-6 months",
                "scalability": 9,
                "innovation_score": 8
            },
            {
                "name": "Sustainable Local Marketplace",
                "tagline": "Connect conscious consumers with eco-friendly local businesses",
                "description": "Mobile-first marketplace that helps users discover, compare, and purchase from local sustainable businesses with verified environmental impact scores.",
                "market_opportunity": "Growing environmental consciousness and support for local businesses",
                "target_customers": "Environmentally conscious millennials and Gen Z consumers",
                "revenue_model": "Commission from sales + premium business listings",
                "competitive_advantage": "Verified sustainability scoring system and hyperlocal focus",
                "market_potential": 8,
                "skills_match": 7 if 'sustainability' in interests or 'marketing' in skills else 5,
                "risk_level": "Medium - Market timing is favorable but requires network effects",
                "capital_required": "$30,000 - $80,000",
                "time_to_market": "3-5 months",
                "scalability": 8,
                "innovation_score": 7
            },
            {
                "name": "Remote Team Wellness Platform",
                "tagline": "Boost productivity and mental health for distributed teams",
                "description": "Comprehensive wellness platform combining AI-powered mood tracking, virtual team building activities, and personalized productivity coaching for remote workers.",
                "market_opportunity": "Remote work is permanent for 35% of workforce, wellness is priority",
                "target_customers": "HR managers, team leaders, remote-first companies",
                "revenue_model": "Per-employee monthly fee ($15-$45/employee)",
                "competitive_advantage": "Combines wellness, productivity, and team building in one platform",
                "market_potential": 9,
                "skills_match": 8 if 'hr' in skills or 'wellness' in interests else 6,
                "risk_level": "Low - Proven market need and low technical complexity",
                "capital_required": "$20,000 - $50,000",
                "time_to_market": "3-4 months",
                "scalability": 9,
                "innovation_score": 6
            }
        ]

        if risk_tolerance == "Conservative":
            for idea in ideas:
                if idea["risk_level"].startswith("High"):
                    idea["risk_level"] = "Medium - " + idea["risk_level"].split(" - ")[1]

        return ideas[:5]
