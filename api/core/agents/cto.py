from __future__ import annotations  # Add this at the top
from .base import AIAgent
from typing import Optional, Dict, Any, List, Tuple

class CTOAgent(AIAgent):
    def __init__(self):
        super().__init__(
            name="CTO Bot",
            role="Chief Technology Officer",
            expertise="software development, system architecture, technical strategy, and emerging technologies"
        )
        self.selected_idea: Optional[Dict[str, Any]] = None

    def update_context(self, business_idea: Optional[Dict[str, Any]]):
        """Update the agent with current business context"""
        self.selected_idea = business_idea

    def get_tech_plan(self) -> str:
        """Get technical implementation plan from CTO agent"""
        if not self.selected_idea:
            return "❌ Please select a business idea first!"
        research_context = self.create_business_context(self.selected_idea, "Technology and Software Development")
        tech_research = self.get_deep_research_data("software engineer", research_context)
        devops_research = self.get_deep_research_data("devops engineer", research_context)
        prompt = f"""
        As an experienced CTO and technology strategist, create a comprehensive technical implementation plan for this business:

        BUSINESS CONCEPT:
        - Name: {self.selected_idea.get('name', 'Not specified')}
        - Description: {self.selected_idea.get('description', 'Not specified')}
        - Target Customers: {self.selected_idea.get('target_customers', 'Not specified')}
        - Revenue Model: {self.selected_idea.get('revenue_model', 'Not specified')}
        - Budget: {self.selected_idea.get('capital_required', 'Not specified')}

        MARKET RESEARCH DATA:

        **Software Engineering Market:**
        {tech_research}
    
        **DevOps/Infrastructure Market:**
        {devops_research}

        Create a detailed technical strategy that includes:

        1. **TECHNOLOGY STACK RECOMMENDATIONS**
        - Frontend technologies (with specific frameworks/libraries)
        - Backend architecture and database choices
        - Cloud infrastructure recommendations
        - Third-party integrations and APIs
        - Development tools and DevOps pipeline

        2. **TEAM BUILDING STRATEGY** (Based on Market Research)
        - Critical technical hires and timeline
        - Skill requirements based on market availability
        - Compensation benchmarks from research data
        - Recruitment strategy for competitive market

        3. **MVP DEVELOPMENT ROADMAP**
        - Phase 1: Core features (must-have for launch)
        - Phase 2: Enhanced features (nice-to-have)
        - Phase 3: Scale features (for growth)
        - Estimated development timeline for each phase

        4. **TECHNICAL ARCHITECTURE**
        - System architecture diagram description
        - Data flow and user journey mapping
        - Scalability considerations
        - Performance optimization strategies

        5. **SECURITY & COMPLIANCE**
        - Data protection and privacy measures
        - Security best practices implementation
        - Compliance requirements (GDPR, CCPA, etc.)
        - Risk mitigation strategies

        6. **DEVELOPMENT RESOURCES & MARKET INSIGHTS**
        - Team composition based on market availability
        - Estimated development costs with market benchmarks
        - Timeline milestones considering hiring challenges
        - Critical technical decisions and trade-offs

        7. **TECHNOLOGY RISKS & MITIGATION**
        - Potential technical challenges
        - Market technology trends to consider
        - Backup plans and alternatives
        - Talent acquisition risks from market research

        Use the market research data to inform hiring strategies, compensation planning, and team building recommendations.
        """
        plan = self.get_response(prompt, "Integrate market research insights to provide data-driven technical guidance that considers real talent market conditions.")
        return f"👨‍💻 **CTO Bot's Technical Implementation Plan:**\n*Enhanced with real-time tech talent market research*\n\n{plan}"
    
    async def chat(self, message: str, history: Optional[List[Dict[str, Any]]] = None) -> Tuple[str, List[Dict[str, Any]]]:
        """Handle interactive chat"""
        if not self.selected_idea:
            return "❌ Please select a business idea first!", history or []

        # Load research data if needed
        if 'research_data' not in self.context_data:
            research_context = self.create_business_context(
                self.selected_idea,
                "Technology and Software Development"
            )
            tech_research = self.get_deep_research_data(
                "software engineer", 
                research_context
            )
            self.update_context(research_data=tech_research)

        # Process the chat message
        response = await self.get_response(
            message,
            context=self._build_context(),
            chat_history=history
        )
        
        # Update history
        updated_history = (history or []) + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": response}
        ]
        
        return response, updated_history

    def _build_context(self) -> str:
        """Build context string for chat"""
        context = f"Business: {self.selected_idea.get('name', 'Startup')}\n"
        context += f"Description: {self.selected_idea.get('description', '')}\n"
        if 'research_data' in self.context_data:
            context += f"\nResearch Data:\n{self.context_data['research_data']}"
        return context