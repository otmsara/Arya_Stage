from .base_agent import AIAgent
from typing import Dict

class SalesAgent(AIAgent):
    def __init__(self):
        super().__init__(
            name="Sales Bot",
            role="Chief Revenue Officer",
            expertise="sales strategy and customer acquisition"
        )
    
    def generate_sales_plan(self, business_idea: Dict) -> str:
        """Generate revenue strategy"""
        research_context = self._create_business_context(business_idea)
        sales_research = self.get_deep_research_data("sales manager", research_context)
        bizdev_research = self.get_deep_research_data("business development manager", research_context)

        prompt = f"""
        Develop sales strategy for: {business_idea['name']}
        Revenue Model: {business_idea.get('revenue_model', 'Not specified')}
        
        Sales Talent Data:
        {sales_research}
        
        Business Development Data:
        {bizdev_research}
        """

        instructions = """
        Provide:
        1. Sales process design
        2. Team structure with hiring plan
        3. Compensation structures from research
        4. Customer acquisition costs
        """
        
        return self.get_response(prompt, instructions)