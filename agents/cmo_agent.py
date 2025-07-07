from .base_agent import AIAgent
from typing import Dict

class CMOAgent(AIAgent):
    def __init__(self):
        super().__init__(
            name="CMO Bot",
            role="Chief Marketing Officer",
            expertise="digital marketing and growth strategies"
        )
    
    def generate_marketing_plan(self, business_idea: Dict) -> str:
        """Generate go-to-market strategy"""
        research_context = self._create_business_context(business_idea)
        marketing_research = self.get_deep_research_data("digital marketing manager", research_context)
        growth_research = self.get_deep_research_data("growth marketing specialist", research_context)

        prompt = f"""
        Develop marketing strategy for: {business_idea['name']}
        Description: {business_idea['description']}
        Target Customers: {business_idea.get('target_customers', 'Not specified')}
        
        Marketing Talent Data:
        {marketing_research}
        
        Growth Specialist Data:
        {growth_research}
        """

        instructions = """
        Include:
        1. Target customer analysis
        2. Marketing team strategy based on research
        3. Digital marketing channels
        4. Budget allocation using market data
        """
        
        return self.get_response(prompt, instructions)