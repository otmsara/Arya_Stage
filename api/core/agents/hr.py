from .base import AIAgent
from typing import Optional, Dict, Any

class HRAgent(AIAgent):
    def __init__(self):
        super().__init__(
            name="HR Bot",
            role="Chief People Officer",
            expertise="talent acquisition, organizational development, culture building, and employee relations"
        )
        self.selected_idea: Optional[Dict[str, Any]] = None

    def update_context(self, business_idea: Dict[str, Any]):
        """Update the agent with current business context"""
        self.selected_idea = business_idea

    def get_hr_plan(self) -> str:
        """Get people strategy from HR agent"""
        if not self.selected_idea:
            return "❌ Please select a business idea first!"

        research_context = self.hr_agent.create_business_context(self.selected_idea, "Human Resources and Talent Management")
        hr_research = self.hr_agent.get_deep_research_data("hr manager", research_context)
        recruiter_research = self.hr_agent.get_deep_research_data("technical recruiter", research_context)

        prompt = f"""
        As an experienced Chief People Officer and HR strategist, create a comprehensive people and culture strategy for this startup:

        BUSINESS CONCEPT:
        - Name: {self.selected_idea.get('name', 'Not specified')}
        - Description: {self.selected_idea.get('description', 'Not specified')}
        - Target Customers: {self.selected_idea.get('target_customers', 'Not specified')}
        - Capital Required: {self.selected_idea.get('capital_required', 'Not specified')}
        - Time to Market: {self.selected_idea.get('time_to_market', 'Not specified')}

        HR TALENT MARKET RESEARCH:

        **HR Professionals:**
        {hr_research}

        **Technical Recruiters:**
        {recruiter_research}

        Develop a detailed people strategy including:

        1. **ORGANIZATIONAL DESIGN & HIRING ROADMAP**
        - Critical first hires (priorities and timeline)
        - Organizational chart evolution (0-10, 10-50, 50+ employees)
        - Role definitions and job descriptions
        - Reporting structures and spans of control
        - Remote vs. hybrid vs. in-office strategy

        2. **TALENT ACQUISITION STRATEGY** (Market-Informed)
        - Sourcing channels for each role type based on market conditions
        - Competitive positioning in talent market
        - Salary benchmarking using research data
        - Recruitment timeline expectations from market research
        - When to hire internal recruiters vs. external agencies

        3. **HR TEAM BUILDING** (Based on Market Research)
        - When to hire first HR professional
        - HR service costs and budget planning
        - Essential HR expertise vs. outsourced functions
        - Scaling HR team with business growth

        4. **COMPANY CULTURE & VALUES**
        - Core values definition and behavioral examples
        - Culture manifestation in daily operations
        - Onboarding experience design
        - Communication protocols and tools
        - Decision-making frameworks

        5. **PERFORMANCE & DEVELOPMENT**
        - Goal-setting methodologies (OKRs, KPIs)
        - Performance review cycles and formats
        - Career development and progression paths
        - Learning and development programs
        - Mentorship and coaching frameworks

        6. **COMPENSATION & BENEFITS** (Market-Benchmarked)
        - Salary bands based on research data
        - Equity guidelines and vesting schedules
        - Benefits package recommendations (health, retirement, perks)
        - Performance-based incentive structures
        - Geographic pay considerations

        7. **EMPLOYEE EXPERIENCE & RETENTION**
        - Engagement measurement and improvement
        - Work-life balance and wellness programs
        - Recognition and reward systems
        - Exit interview processes
        - Retention strategies for key talent

        8. **COMPLIANCE & RISK MANAGEMENT**
        - Employment law compliance checklist
        - Diversity, equity, and inclusion initiatives
        - Harassment prevention and reporting
        - Employee handbook and policy development
        - HR technology and systems recommendations

        9. **SCALING CONSIDERATIONS** (Research-Informed)
        - HR metrics and analytics to track
        - Budget planning for HR function growth
        - Outsourcing vs. in-house HR functions
        - Cultural preservation during rapid growth
        - Change management strategies

        Use market research to inform hiring timelines, compensation planning, and HR resource allocation decisions.
        """
        plan = self.hr_agent.get_response(prompt, "Integrate market research insights to create a realistic people strategy that accounts for talent market conditions and competitive dynamics.")
        return f"👥 **HR Bot's People & Culture Strategy:**\n*Enhanced with HR talent market intelligence*\n\n{plan}"
    