from .base_agent import AIAgent
from typing import Dict

class CFOAgent(AIAgent):
    def __init__(self):
        super().__init__(
            name="CFO Bot",
            role="Chief Financial Officer", 
            expertise="financial modeling and fundraising"
        )
    
    def generate_financial_plan(self, business_idea: Dict) -> str:
        """Generate 3-year financial projections"""
        research_context = self._create_business_context(business_idea)
        finance_research = self.get_deep_research_data("financial analyst", research_context)
        ops_research = self.get_deep_research_data("business operations manager", research_context)

        prompt = f"""
        Create financial model for: {business_idea['name']}
        Revenue Model: {business_idea.get('revenue_model', 'Not specified')}
        Capital Required: {business_idea.get('capital_required', 'Not specified')}
        
        Financial Talent Data:
        {finance_research}
        
        Operations Data:
        {ops_research}
        """

        instructions = """
        Provide:
        1. 3-year revenue projections
        2. Cost structure analysis
        3. Funding requirements
        4. Salary benchmarks from research
        """
        
        return self.get_response(prompt, instructions)