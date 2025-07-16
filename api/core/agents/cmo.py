from .base import AIAgent
from typing import Optional, Dict, Any

class CMOAgent(AIAgent):
    def __init__(self):
        super().__init__(
            name="CMO Bot",
            role="Chief Marketing Officer",
            expertise="digital marketing, customer acquisition, brand strategy, and growth hacking"
        )
        self.selected_idea: Optional[Dict[str, Any]] = None

    def update_context(self, business_idea: Optional[Dict[str, Any]]):
        """Update the agent with current business context"""
        self.selected_idea = business_idea

    def get_marketing_plan(self) -> str:
        """Get marketing strategy from CMO agent"""
        if not self.selected_idea:
            return "❌ Please select a business idea first!"

        research_context = self.cmo_agent.create_business_context(self.selected_idea, "Digital Marketing and Growth")
        marketing_research = self.cmo_agent.get_deep_research_data("digital marketing manager", research_context)
        growth_research = self.cmo_agent.get_deep_research_data("growth marketing specialist", research_context)

        prompt = f"""
        As an experienced CMO and growth strategist, develop a comprehensive go-to-market strategy for this business:

        BUSINESS CONCEPT:
        - Name: {self.selected_idea.get('name', 'Not specified')}
        - Description: {self.selected_idea.get('description', 'Not specified')}
        - Target Customers: {self.selected_idea.get('target_customers', 'Not specified')}
        - Revenue Model: {self.selected_idea.get('revenue_model', 'Not specified')}
        - Competitive Advantage: {self.selected_idea.get('competitive_advantage', 'Not specified')}
        - Budget: {self.selected_idea.get('capital_required', 'Not specified')}

        MARKETING TALENT MARKET RESEARCH:

        **Digital Marketing Professionals:**
        {marketing_research}

        **Growth Marketing Specialists:**
        {growth_research}

        Create a detailed marketing strategy that includes:

        1. **TARGET CUSTOMER ANALYSIS**
        - Detailed customer personas (demographics, psychographics, pain points)
        - Customer journey mapping
        - Market segmentation strategy
        - Customer lifetime value estimates

        2. **MARKETING TEAM STRATEGY** (Based on Market Research)
        - Essential marketing hires and timeline
        - Skills assessment based on market availability
        - Compensation planning using research benchmarks
        - Recruitment strategy for competitive talent market

        3. **BRAND POSITIONING & MESSAGING**
        - Unique value proposition refinement
        - Brand personality and voice
        - Key messaging pillars
        - Competitive differentiation strategy

        4. **DIGITAL MARKETING STRATEGY**
        - Primary acquisition channels (with specific tactics)
        - Content marketing plan
        - Social media strategy
        - SEO/SEM recommendations
        - Email marketing automation

        5. **LAUNCH STRATEGY**
        - Pre-launch buzz building (90 days before)
        - Launch week execution plan
        - Post-launch growth tactics
        - Milestone-based marketing calendar

        6. **CUSTOMER ACQUISITION**
        - Cost per acquisition targets by channel
        - Conversion funnel optimization
        - Referral and viral growth strategies
        - Partnership and collaboration opportunities

        7. **BUDGET ALLOCATION & TEAM COSTS**
        - Marketing spend breakdown by channel
        - Team salary costs based on market research
        - Expected ROI for each channel
        - Testing and optimization budget
        - Performance tracking KPIs

        8. **GROWTH HACKING TACTICS**
        - Creative, low-cost acquisition strategies
        - Viral mechanics and network effects
        - Community building approaches
        - Influencer and partnership strategies

        Use market research to inform team building, budget planning, and competitive positioning strategies.
        """
        plan = self.cmo_agent.get_response(prompt, "Leverage market research data to create realistic marketing strategies that account for talent costs and market conditions.")
        return f"📢 **CMO Bot's Go-to-Market Strategy:**\n*Enhanced with marketing talent market insights*\n\n{plan}"
