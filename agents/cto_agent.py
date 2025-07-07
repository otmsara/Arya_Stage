from .base_agent import AIAgent

class CTOAgent(AIAgent):
    def __init__(self):
        super().__init__(
            name="CTO Bot",
            role="Chief Technology Officer",
            expertise="software architecture and technical strategy"
        )
    
    def generate_tech_plan(self, business_idea: Dict) -> str:
        """Generate technical implementation plan"""
        if not business_idea:
            return "Error: No business idea provided"
            
        research_context = self._create_business_context(business_idea)
        tech_research = self.get_deep_research_data("software engineer", research_context)
        
        prompt = f"""
        Create technical plan for: {business_idea['name']}
        Description: {business_idea['description']}
        Research Data: {tech_research}
        """
        
        return self.get_response(
            prompt,
            "Provide detailed technical strategy including stack, architecture, and team plan"
        )
    
    def _create_business_context(self, idea: Dict) -> str:
        return f"""
        Business: {idea.get('name')}
        Description: {idea.get('description')}
        Budget: {idea.get('capital_required')}
        """