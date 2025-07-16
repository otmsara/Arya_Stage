from .base import AIAgent
from typing import Optional, Dict, Any

class SalesAgent(AIAgent):
    def __init__(self):
        super().__init__(
            name="Sales Bot",
            role="Chief Revenue Officer",
            expertise="sales strategy, revenue optimization, customer success, and business development"
        )
        self.selected_idea: Optional[Dict[str, Any]] = None

    def update_context(self, business_idea: Optional[Dict[str, Any]]):
        """Update the agent with current business context"""
        self.selected_idea = business_idea

    def get_sales_plan(self) -> str:
        """Get sales strategy from Sales agent"""
        if not self.selected_idea:
            return "❌ Please select a business idea first!"

        research_context = self.sales_agent.create_business_context(self.selected_idea, "Sales and Business Development")
        sales_research = self.sales_agent.get_deep_research_data("sales manager", research_context)
        biz_dev_research = self.sales_agent.get_deep_research_data("business development manager", research_context)

        prompt = f"""
        As an experienced Chief Revenue Officer and sales strategist, create a comprehensive revenue generation strategy for this startup:

        BUSINESS CONCEPT:
        - Name: {self.selected_idea.get('name', 'Not specified')}
        - Description: {self.selected_idea.get('description', 'Not specified')}
        - Target Customers: {self.selected_idea.get('target_customers', 'Not specified')}
        - Revenue Model: {self.selected_idea.get('revenue_model', 'Not specified')}
        - Competitive Advantage: {self.selected_idea.get('competitive_advantage', 'Not specified')}

        SALES TALENT MARKET RESEARCH:

        **Sales Professionals:**
        {sales_research}

        **Business Development Managers:**
        {biz_dev_research}

        Develop a detailed sales and revenue strategy including:

        1. **SALES STRATEGY & METHODOLOGY**
        - Sales process design (lead to close)
        - Sales methodology selection (SPIN, Challenger, etc.)
        - Customer journey mapping and touchpoint optimization
        - Sales cycle analysis and acceleration tactics
        - Win/loss analysis framework

        2. **SALES TEAM STRATEGY** (Market-Informed)
        - Sales hiring roadmap and timeline
        - Role definitions and skill requirements
        - Compensation structures based on market research
        - When to hire sales professionals vs. founder-led sales
        - Scaling sales team with revenue growth

        3. **CUSTOMER SEGMENTATION & TARGETING**
        - Ideal Customer Profile (ICP) definition
        - Market segmentation and prioritization
        - Account-based selling strategies
        - Vertical market penetration plans
        - Geographic expansion roadmap

        4. **PRICING & REVENUE OPTIMIZATION**
        - Pricing strategy and tier structure
        - Value-based pricing models
        - Discount and negotiation guidelines
        - Upselling and cross-selling opportunities
        - Revenue recognition and billing strategies

        5. **SALES PROCESS & TECHNOLOGY**
        - CRM selection and implementation
        - Sales automation and workflow design
        - Lead qualification and scoring
        - Proposal and contract management
        - Sales analytics and reporting dashboards

        6. **SALES BUDGET & RESOURCE PLANNING** (Research-Based)
        - Sales team costs using market benchmarks
        - Sales technology and tools budget
        - Territory planning and quota allocation
        - Commission and incentive structures
        - ROI expectations and timeline

        7. **CUSTOMER SUCCESS & RETENTION**
        - Onboarding and implementation process
        - Customer health scoring and monitoring
        - Renewal and expansion strategies
        - Churn reduction initiatives
        - Customer advocacy and reference programs

        8. **PARTNERSHIP & CHANNEL STRATEGY**
        - Channel partner identification and recruitment
        - Partner enablement and support programs
        - Strategic alliance opportunities
        - Referral program design
        - Co-selling and co-marketing initiatives

        9. **SALES OPERATIONS & METRICS**
        - Key performance indicators (KPIs) and targets
        - Sales forecasting and pipeline management
        - Performance tracking and optimization
        - Sales process improvement methodology
        - Competitive intelligence gathering

        10. **GO-TO-MARKET EXECUTION** (Market-Validated)
        - Launch strategy and timeline
        - Early customer acquisition tactics
        - Pilot program and beta customer management
        - Market feedback integration
        - Scaling strategies post-product-market fit

        Use market research data to inform sales team building, compensation planning, and competitive positioning strategies.
        """
        plan = self.sales_agent.get_response(prompt, "Leverage market research to design a comprehensive sales strategy that accounts for talent costs, market conditions, and competitive dynamics.")
        return f"💼 **Sales Bot's Revenue Generation Strategy:**\n*Enhanced with sales talent market research*\n\n{plan}"
    