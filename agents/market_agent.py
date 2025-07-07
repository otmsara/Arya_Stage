from .base_agent import AIAgent
from typing import Dict

class MarketResearchAgent(AIAgent):
    def __init__(self):
        super().__init__(
            name="Market Research Bot",
            role="Market Intelligence Analyst",
            expertise="competitive analysis and market sizing"
        )
    
    def generate_market_analysis(self, business_idea: Dict) -> str:
        """Generate competitive intelligence report"""
        research_context = self._create_business_context(business_idea)
        market_research = self.get_deep_research_data("market research analyst", research_context)

        prompt = f"""
        Analyze market for: {business_idea['name']}
        Target Market: {business_idea.get('target_customers', 'Not specified')}
        
        Competitive Data:
        {market_research}
        """

        instructions = """
        Include:
        1. Market size (TAM/SAM/SOM)
        2. Competitive landscape
        3. Customer segmentation
        4. Barriers to entry
        """
        
        return self.get_response(prompt, instructions)