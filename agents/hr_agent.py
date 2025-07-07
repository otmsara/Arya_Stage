from .base_agent import AIAgent
from typing import Dict

class HRAgent(AIAgent):
    def __init__(self):
        super().__init__(
            name="HR Bot",
            role="Chief People Officer",
            expertise="talent acquisition and organizational development"
        )
    
    def generate_hr_plan(self, business_idea: Dict) -> str:
        """Generate people strategy"""
        research_context = self._create_business_context(business_idea)
        hr_research = self.get_deep_research_data("hr manager", research_context)
        recruiter_research = self.get_deep_research_data("technical recruiter", research_context)

        prompt = f"""
        Create HR strategy for: {business_idea['name']}
        Stage: Startup
        Planned Team Size: 10-50
        
        HR Talent Data:
        {hr_research}
        
        Recruiter Data:
        {recruiter_research}
        """

        instructions = """
        Include:
        1. Hiring roadmap with timelines
        2. Compensation benchmarks
        3. Company culture framework
        4. Remote work policy based on research
        """
        
        return self.get_response(prompt, instructions)