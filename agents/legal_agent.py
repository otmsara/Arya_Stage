from .base_agent import AIAgent
from typing import Dict

class LegalAgent(AIAgent):
    def __init__(self):
        super().__init__(
            name="Legal Bot",
            role="Chief Legal Officer",
            expertise="corporate law and compliance"
        )
    
    def generate_legal_plan(self, business_idea: Dict) -> str:
        """Generate legal framework"""
        research_context = self._create_business_context(business_idea)
        legal_research = self.get_deep_research_data("legal counsel", research_context)
        compliance_research = self.get_deep_research_data("compliance officer", research_context)

        prompt = f"""
        Develop legal strategy for: {business_idea['name']}
        Industry: {business_idea.get('industry', 'Technology')}
        
        Legal Talent Data:
        {legal_research}
        
        Compliance Data:
        {compliance_research}
        """

        instructions = """
        Cover:
        1. Business structure recommendations
        2. Intellectual property strategy  
        3. Regulatory compliance
        4. Legal budget based on market rates
        """
        
        return self.get_response(prompt, instructions)