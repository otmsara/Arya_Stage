from .base import AIAgent
from typing import Optional, Dict, Any


class CFOAgent(AIAgent):
    def __init__(self):
        super().__init__("CFO Bot", "Chief Financial Officer", "financial modeling, fundraising, business planning, and investment strategy")
        self.selected_idea: Optional[Dict[str, Any]] = None

    def update_context(self, business_idea: Optional[Dict[str, Any]]):
        """Update the agent with current business context"""
        self.selected_idea = business_idea
        
    def get_financial_plan(self) -> str:
        """Get financial model from CFO agent"""
        if not self.selected_idea:
            return "❌ Please select a business idea first!"

        research_context = self.cfo_agent.create_business_context(self.selected_idea, "Finance and Business Operations")
        finance_research = self.cfo_agent.get_deep_research_data("financial analyst", research_context)
        operations_research = self.cfo_agent.get_deep_research_data("business operations manager", research_context)

        prompt = f"""
        As an experienced CFO and financial strategist, create a comprehensive financial model and business plan for this venture:

        BUSINESS CONCEPT:
        - Name: {self.selected_idea.get('name', 'Not specified')}
        - Description: {self.selected_idea.get('description', 'Not specified')}
        - Revenue Model: {self.selected_idea.get('revenue_model', 'Not specified')}
        - Target Customers: {self.selected_idea.get('target_customers', 'Not specified')}
        - Capital Required: {self.selected_idea.get('capital_required', 'Not specified')}
        - Time to Market: {self.selected_idea.get('time_to_market', 'Not specified')}

        FINANCIAL TALENT MARKET RESEARCH:

        **Financial Professionals:**
        {finance_research}

        **Operations Managers:**
        {operations_research}

        Develop a detailed financial analysis including:

        1. **REVENUE PROJECTIONS (3-Year Model)**
            - Monthly revenue projections for Year 1
            - Quarterly projections for Years 2-3
            - Revenue drivers and assumptions
            - Pricing strategy and optimization
            - Customer acquisition and retention rates

        2. **COST STRUCTURE ANALYSIS** (Enhanced with Market Data)
            - Fixed c    osts (overhead, salaries based on market research, rent, software)
            - Variable costs (per customer/transaction)
            - Team salary costs using research benchmarks
            - Customer acquisition costs (CAC) by channel
            - Cost optimization opportunities

        3. **TEAM FINANCIAL PLANNING** (Based on Market Research)
            - Hiring costs and timeline for key financial roles
            - Salary benchmarks from research data
            - Equity compensation strategies
            - When to hire financial professionals vs. outsource

        4. **FINANCIAL METRICS & KPIs**
            - Unit economics (LTV/CAC ratio)
            - Gross margin and contribution margin
            - Monthly recurring revenue (if applicable)
            - Cash flow projections
            - Break-even analysis

        5. **FUNDING REQUIREMENTS**
            - Initial capital needs breakdown including team costs
            - Cash flow timing and funding milestones
            - Runway calculations with realistic salary costs
            - Potential funding sources (bootstrapping, angels, VCs)

        6. **INVESTMENT RETURNS**
            - ROI projections for investors
            - Exit scenarios and valuations
            - Comparable company analysis
            - Risk-adjusted returns

        7. **SCENARIO PLANNING**
            - Best case, base case, worst case scenarios
            - Sensitivity analysis for key variables including talent costs
            - Risk factors and mitigation strategies
            - Pivot scenarios and financial impact

        8. **FUNDRAISING STRATEGY**
            - Funding rounds and timing
            - Valuation benchmarks
            - Investor targeting strategy
            - Key financial milestones for each round

        Use market research data to provide realistic salary projections and hiring cost estimates.
        """
        plan = self.cfo_agent.get_response(prompt, "Integrate market research to create realistic financial projections that account for actual talent costs and market conditions.")
        return f"💰 **CFO Bot's Financial Model & Business Plan:**\n*Enhanced with financial talent market benchmarks*\n\n{plan}"
