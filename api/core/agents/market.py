from .base import AIAgent
from typing import Optional, Dict, Any

class MarketResearchAgent(AIAgent):
    def __init__(self):
        super().__init__(
            name="Market Research Bot",
            role="Market Intelligence Analyst",
            expertise="competitive analysis, market sizing, trend analysis, and customer research"
        )
        self.selected_idea: Optional[Dict[str, Any]] = None

    def update_context(self, business_idea: Optional[Dict[str, Any]]):
        """Update the agent with current business context"""
        self.selected_idea = business_idea

    def get_market_research(self) -> str:
        """Get market analysis from Market Research agent"""
        if not self.selected_idea:
            return "❌ Please select a business idea first!"
        
        research_context = self.market_agent.create_business_context(self.selected_idea, "Market Analysis and Competitive Intelligence")
        competitor_research = self.market_agent.get_deep_research_data("market research analyst", research_context)

        prompt = f"""
        As a senior market research analyst, conduct comprehensive market intelligence for this business:

        BUSINESS CONCEPT:
        - Name: {self.selected_idea.get('name', 'Not specified')}
        - Description: {self.selected_idea.get('description', 'Not specified')}
        - Target Market: {self.selected_idea.get('target_customers', 'Not specified')}

        MARKET RESEARCH DATA:

        **Competitive Intelligence:**
        {competitor_research}

        Provide detailed analysis including:

        1. **MARKET SIZE & OPPORTUNITY**
        - Total Addressable Market (TAM)
        - Serviceable Addressable Market (SAM)
        - Serviceable Obtainable Market (SOM)
        - Market growth rate and trends
        - Geographic expansion opportunities

        2. **COMPETITIVE LANDSCAPE** (Enhanced with Research Data)
        - Direct and indirect competitors from research
        - Market share analysis
        - Competitive positioning map
        - Pricing comparison based on market data
        - Strengths and weaknesses analysis

        3. **CUSTOMER RESEARCH**
        - Customer persona validation
        - Pain point analysis
        - Buying behavior patterns
        - Decision-making process
        - Price sensitivity analysis

        4. **MARKET TRENDS & DRIVERS**
        - Industry growth catalysts
        - Technology disruption factors
        - Regulatory changes impact
        - Economic factors influence
        - Social and cultural shifts

        5. **MARKET ENTRY STRATEGY** (Data-Informed)
        - Optimal market entry timing based on research
        - Geographic prioritization
        - Customer segment sequencing
        - Partnership opportunities identified in research
        - Barriers to entry assessment

        Use the competitive research data to enhance market analysis and strategic recommendations.
        """
        plan = self.market_agent.get_response(prompt, "Integrate market research data to provide comprehensive, data-driven market intelligence and competitive analysis.")
        return f"📊 **Market Research Bot's Intelligence Report:**\n*Enhanced with competitive market data*\n\n{plan}"
