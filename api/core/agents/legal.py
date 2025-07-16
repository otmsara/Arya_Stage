from .base import AIAgent
from typing import Optional, Dict, Any

class LegalAgent(AIAgent):
    def __init__(self):
        super().__init__(
            name="Legal Bot",
            role="Chief Legal Officer",
            expertise="business law, corporate structure, contracts, intellectual property, and regulatory compliance"
        )
        self.selected_idea: Optional[Dict[str, Any]] = None

    def update_context(self, business_idea: Optional[Dict[str, Any]]):
        """Update the agent with current business context"""
        self.selected_idea = business_idea

    def get_legal_plan(self) -> str:
        """Get legal framework from Legal agent"""
        if not self.selected_idea:
            return "❌ Please select a business idea first!"

        research_context = self.legal_agent.create_business_context(self.selected_idea, "Legal and Compliance")
        legal_research = self.legal_agent.get_deep_research_data("legal counsel", research_context)
        compliance_research = self.legal_agent.get_deep_research_data("compliance officer", research_context)

        prompt = f"""
        As an experienced business attorney and legal strategist, create a comprehensive legal framework for this startup:

        BUSINESS CONCEPT:
        - Name: {self.selected_idea.get('name', 'Not specified')}
        - Description: {self.selected_idea.get('description', 'Not specified')}
        - Target Customers: {self.selected_idea.get('target_customers', 'Not specified')}
        - Revenue Model: {self.selected_idea.    get('revenue_model', 'Not specified')}
        - Market Opportunity: {self.selected_idea.get('market_opportunity', 'Not specified')}

        LEGAL TALENT MARKET RESEARCH:

        **Legal Counsel Market:**
        {legal_research}

        **Compliance Professionals:**
        {compliance_research}

        Develop a detailed legal strategy including:

        1. **BUSINESS STRUCTURE RECOMMENDATIONS**
        - Entity type selection (LLC, C-Corp, S-Corp analysis)
        - Jurisdiction recommendations (Delaware, home state, etc.)
        - Tax implications and optimization strategies
        - Ownership structure and equity distribution
        - Board composition and governance requirements

        2. **LEGAL TEAM PLANNING** (Based on Market Research)
        - When to hire in-house legal counsel vs. external
        - Legal service costs and budget planning
        - Essential legal expertise needed for your industry
        - Outsourcing strategies for early-stage companies

        3. **INTELLECTUAL PROPERTY STRATEGY**
        - Trademark protection for business name and brand
        - Patent opportunities and filing strategy
        - Copyright protection for content and software
        - Trade secret identification and protection
        - IP assignment agreements for employees/contractors

        4. **REGULATORY COMPLIANCE**
        - Industry-specific regulations and licensing
        - Data privacy and protection (GDPR, CCPA, state laws)
        - Consumer protection requirements
        - Employment law compliance
        - Securities regulations (if fundraising)

        5. **ESSENTIAL LEGAL DOCUMENTS**
        - Founder agreements and equity splits
        - Employment contracts and offer letters
        - Independent contractor agreements
        - Terms of service and privacy policy
        - Customer contracts and service agreements

        6. **RISK MANAGEMENT & LIABILITY**
        - Liability exposure assessment
        - Insurance requirements (general, professional, cyber)
        - Indemnification strategies
        - Limitation of liability clauses
        - Dispute resolution mechanisms

        7. **FUNDRAISING LEGAL PREPARATION**
        - Cap table setup and management
        - Investment document preparation
        - Due diligence readiness checklist
        - Investor protection provisions
        - Anti-dilution and liquidation preferences

        8. **LEGAL BUDGET & RESOURCE PLANNING** (Market-Informed)
        - Legal service cost estimates based on market rates
        - Priority legal work vs. nice-to-have
        - Timeline for different legal milestones
        - When to transition from external to internal legal resources

        Use market research to inform legal service budgeting and resource planning decisions.
        """
        plan = self.legal_agent.get_response(prompt, "Leverage market research to provide realistic legal guidance that accounts for actual service costs and resource availability.")
        return f"⚖️ **Legal Bot's Corporate & Compliance Strategy:**\n*Enhanced with legal services market data*\n\n{plan}"