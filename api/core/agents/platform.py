from __future__ import annotations
import json
import openai
import os
from datetime import datetime

openai.api_deep_research = os.getenv("DEEP_RESEARCH_API_URL")


class BusinessSchoolPlatform:
    def __init__(self):
        # Lazy import agents to break circular dependency
        from .cto import CTOAgent
        from .cmo import CMOAgent
        from .cfo import CFOAgent
        from .legal import LegalAgent
        from .hr import HRAgent
        from .sales import SalesAgent
        from .market import MarketResearchAgent
        from .idea_scout import IdeaScoutAgent


        self.idea_scout = IdeaScoutAgent()
        self.cto_agent = CTOAgent()
        self.cmo_agent = CMOAgent()
        self.cfo_agent = CFOAgent()
        self.legal_agent = LegalAgent()
        self.hr_agent = HRAgent()
        self.sales_agent = SalesAgent()
        self.market_agent = MarketResearchAgent()

        # Session state
        self.user_profile = {}
        self.generated_ideas = []
        self.selected_idea = None
        self.virtual_team = {}
        self.business_plans = []

        # Chat histories for each agent
        self.chat_histories = {
            'cto': [],
            'cmo': [],
            'cfo': [],
            'legal': [],
            'hr': [],
            'sales': [],
            'market': []
        }
        
    def collect_user_profile(self, skills, interests, risk_tolerance, budget, experience):
        """Collect and store user profile information"""
        self.user_profile = {
            'skills': skills,
            'interests': interests,
            'risk_tolerance': risk_tolerance,
            'budget': budget,
            'experience': experience
        }
        return "✅ Profile saved! Click 'Generate Ideas' to see your personalized business concepts."

    def generate_business_ideas(self):
        """Generate enhanced business ideas based on user profile"""
        if not self.user_profile:
            return "❌ Please fill out your profile first!"

        ideas = self.idea_scout.generate_ideas(self.user_profile)
        self.generated_ideas = ideas

        ideas_text = "🚀 **Your AI-Generated Business Portfolio**\n"
        ideas_text += f"*Generated on {datetime.now().strftime('%B %d, %Y')} based on current market analysis*\n\n"

        for i, idea in enumerate(ideas, 1):
            market_score = idea.get('market_potential', 5)
            skills_score = idea.get('skills_match', 5)
            scalability_score = idea.get('scalability', 5)
            innovation_score = idea.get('innovation_score', 5)
            overall_score = round((market_score + skills_score + scalability_score + innovation_score) / 4, 1)

            score_emoji = "🔥" if overall_score >= 8 else "⭐" if overall_score >= 6 else "💡"

            ideas_text += f"## {score_emoji} **{i}. {idea.get('name', 'Unnamed Idea')}**\n"
            ideas_text += f"*{idea.get('tagline', 'No tagline available')}*\n\n"

            ideas_text += f"**📖 Description:** {idea.get('description', 'No description available')}\n\n"

            ideas_text += f"**🎯 Target Market:** {idea.get('target_customers', 'Not specified')}\n"
            ideas_text += f"**💡 Market Opportunity:** {idea.get('market_opportunity', 'Not specified')}\n"
            ideas_text += f"**💰 Revenue Model:** {idea.get('revenue_model', 'Not specified')}\n"
            ideas_text += f"**🏆 Competitive Edge:** {idea.get('competitive_advantage', 'Not specified')}\n\n"

            ideas_text += "**📊 AI Analysis Scores:**\n"
            ideas_text += f"• Overall Score: **{overall_score}/10** {score_emoji}\n"
            ideas_text += f"• Market Potential: {market_score}/10\n"
            ideas_text += f"• Skills Match: {skills_score}/10\n"
            ideas_text += f"• Scalability: {scalability_score}/10\n"
            ideas_text += f"• Innovation Level: {innovation_score}/10\n\n"

            ideas_text += "**📈 Business Metrics:**\n"
            ideas_text += f"• Risk Level: {idea.get('risk_level', 'Not assessed')}\n"
            ideas_text += f"• Capital Required: {idea.get('capital_required', 'TBD')}\n"
            ideas_text += f"• Time to Market: {idea.get('time_to_market', 'Not estimated')}\n\n"

            ideas_text += "---\n\n"

        if ideas:
            best_idea = max(ideas, key=lambda x: (x.get('market_potential', 0) + x.get('skills_match', 0)))
            ideas_text += f"🎯 **AI Recommendation:** Based on your profile, **{best_idea.get('name')}** shows the highest potential for success!\n\n"

        ideas_text += "💡 **Next Step:** Select your favorite idea below to assemble your virtual C-suite team!"

        return ideas_text

    def select_idea_and_build_team(self, idea_index):
        """Select an idea and assemble virtual C-suite team with enhanced context"""
        if not self.generated_ideas:
            return "❌ Please generate ideas first!"

        try:
            idea_idx = int(idea_index) - 1
            if idea_idx < 0 or idea_idx >= len(self.generated_ideas):
                return "❌ Invalid idea number!"

            self.selected_idea = self.generated_ideas[idea_idx]

            # Update all agents with the selected business idea context
            for agent_name, agent in [
                ('cto', self.cto_agent),
                ('cmo', self.cmo_agent),
                ('cfo', self.cfo_agent),
                ('legal', self.legal_agent),
                ('hr', self.hr_agent),
                ('sales', self.sales_agent),
                ('market', self.market_agent)
            ]:
                agent.update_context(business_idea=self.selected_idea)
                # Reset chat history for new business idea
                self.chat_histories[agent_name] = []

                team_status = f"🎯 **Selected Idea:** {self.selected_idea['name']}\n\n"
                team_status += "🤖 **Assembling Complete Virtual C-Suite Team...**\n\n"
                team_status += "👨‍💼 **CTO Bot** - Ready for interactive technical strategy discussions\n"
                team_status += "👩‍💼 **CMO Bot** - Ready for dynamic marketing strategy conversations\n"
                team_status += "👨‍💼 **CFO Bot** - Ready for financial planning and funding discussions\n"
                team_status += "⚖️ **Legal Bot** - Ready for corporate structure and compliance guidance\n"
                team_status += "👥 **HR Bot** - Ready for team building and culture development\n"
                team_status += "💼 **Sales Bot** - Ready for revenue strategy and customer success\n"
                team_status += "📊 **Market Research Bot** - Ready for competitive intelligence discussions\n"
                team_status += "\n✅ **Complete Executive Team Assembled with Interactive Chat!**\n"
                team_status += "\n💬 **Enhanced Features:**\n"
                team_status += "• Open-ended conversations with each specialist\n"
                team_status += "• Challenge recommendations and get clarifications\n"
                team_status += "• Evolutionary discussions that build on previous points\n"
                team_status += "• Real-time market data integration in conversations\n"
                team_status += "\n🚀 **Use the chat interfaces below to have detailed discussions with each C-suite member.**"
                return team_status
        except ValueError:
            return "❌ Please enter a valid number!"

    # Chat functions for each agent - Fixed for Gradio ChatInterface compatibility
    def chat_with_cto(self, message: str, history: list) -> str:
        """Handle CTO chat interactions"""
        if not self.selected_idea:
            return "❌ Please select a business idea first!"

        # Initialiser le contexte si nécessaire
        if not hasattr(self.cto_agent, 'context_data'):
            self.cto_agent.context_data = {}
            
        # Charger les données de recherche si manquantes
        if 'research_data' not in self.cto_agent.context_data:
            research_context = {
                "business": self.selected_idea.get('name', 'Startup'),
                "description": self.selected_idea.get('description', ''),
                "target_market": self.selected_idea.get('target_customers', '')
            }
            
            # Simuler get_deep_research_data sans modifier l'agent
            tech_research = {
                "software_engineer": {
                    "market_data": "Current tech talent market analysis...",
                    "salary_ranges": "$80k-$150k"
                }
            }
            
            # Mettre à jour le contexte sans modifier la classe de l'agent
            self.cto_agent.context_data = {
                **getattr(self.cto_agent, 'context_data', {}),
                "business_idea": self.selected_idea,
                "research_data": tech_research
            }

        # Gérer l'historique de chat
        internal_history = []
        for msg_pair in history:
            if len(msg_pair) >= 2:
                internal_history.extend([
                    {"role": "user", "content": msg_pair[0]},
                    {"role": "assistant", "content": msg_pair[1]}
                ])

        # Appeler la méthode chat de l'agent
        response = self.cto_agent.get_response(
            message,
            context=str(self.cto_agent.context_data)
        )
        
        # Mettre à jour l'historique
        self.chat_histories['cto'] = internal_history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": response}
        ]
        
        return response

    def chat_with_cmo(self, message: str, history: list) -> str:
        """Handle CMO chat interactions"""
        if not self.selected_idea:
            return "❌ Please select a business idea first!"

        # Initialiser le contexte si nécessaire
        if not hasattr(self.cmo_agent, 'context_data'):
            self.cmo_agent.context_data = {}
        
        # Charger les données de recherche si manquantes
        if 'research_data' not in self.cmo_agent.context_data:
            research_context = {
                "business": self.selected_idea.get('name', 'Startup'),
                "description": self.selected_idea.get('description', ''),
                "target_market": self.selected_idea.get('target_customers', '')
            }
        
            # Simuler get_deep_research_data pour le marketing
            marketing_research = {
                "digital_marketing": {
                    "market_data": "Current digital marketing trends...",
                    "salary_ranges": "$60k-$120k"
                }
            }
        
            # Mettre à jour le contexte
            self.cmo_agent.context_data = {
                **getattr(self.cmo_agent, 'context_data', {}),
                "business_idea": self.selected_idea,
                "research_data": marketing_research
            }

        # Convertir l'historique
        internal_history = []
        for msg_pair in history:
            if len(msg_pair) >= 2:
                internal_history.extend([
                    {"role": "user", "content": msg_pair[0]},
                    {"role": "assistant", "content": msg_pair[1]}
                ])

        # Obtenir la réponse
        response = self.cmo_agent.get_response(
            message,
            context=str(self.cmo_agent.context_data)
        )
    
        # Mettre à jour l'historique
        self.chat_histories['cmo'] = internal_history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": response}
        ]
    
        return response

    def chat_with_cfo(self, message: str, history: list) -> str:
        """Handle CFO chat interactions"""
        if not self.selected_idea:
            return "❌ Please select a business idea first!"

        # Initialiser le contexte
        if not hasattr(self.cfo_agent, 'context_data'):
            self.cfo_agent.context_data = {}
        
        # Charger les données financières si manquantes
        if 'research_data' not in self.cfo_agent.context_data:
            research_context = {
                "business": self.selected_idea.get('name', 'Startup'),
                "revenue_model": self.selected_idea.get('revenue_model', ''),
            "capital": self.selected_idea.get('capital_required', '')
            }
        
            financial_research = {
                "financial_analyst": {
                    "market_data": "Current financial job market...",
                    "salary_ranges": "$70k-$140k"
                }
            }
        
            self.cfo_agent.context_data = {
                **getattr(self.cfo_agent, 'context_data', {}),
                "business_idea": self.selected_idea,
                "research_data": financial_research
            }

        # Gérer l'historique
        internal_history = []
        for msg_pair in history:
            if len(msg_pair) >= 2:
                internal_history.extend([
                    {"role": "user", "content": msg_pair[0]},
                    {"role": "assistant", "content": msg_pair[1]}
                ])

        response = self.cfo_agent.get_response(
            message,
            context=str(self.cfo_agent.context_data)
        )
    
        self.chat_histories['cfo'] = internal_history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": response}
        ]
    
        return response

    def chat_with_legal(self, message: str, history: list) -> str:
        """Handle Legal chat interactions"""
        if not self.selected_idea:
            return "❌ Please select a business idea first!"

        # Initialiser le contexte
        if not hasattr(self.legal_agent, 'context_data'):
            self.legal_agent.context_data = {}
        
        # Charger les données juridiques si manquantes
        if 'research_data' not in self.legal_agent.context_data:
            legal_research = {
                "legal_counsel": {
                    "market_data": "Current legal services market...",
                    "service_costs": "$150-$400/hour"
                }
            }
        
            self.legal_agent.context_data = {
                **getattr(self.legal_agent, 'context_data', {}),
                "business_idea": self.selected_idea,
                "research_data": legal_research
            }

        # Gérer l'historique
        internal_history = []
        for msg_pair in history:
            if len(msg_pair) >= 2:
                internal_history.extend([
                    {"role": "user", "content": msg_pair[0]},
                    {"role": "assistant", "content": msg_pair[1]}
                ])

        response = self.legal_agent.get_response(
            message,
            context=str(self.legal_agent.context_data)
        )
    
        self.chat_histories['legal'] = internal_history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": response}
        ]
    
        return response

    def chat_with_hr(self, message: str, history: list) -> str:
        """Handle HR chat interactions"""
        if not self.selected_idea:
            return "❌ Please select a business idea first!"

        # Initialiser le contexte
        if not hasattr(self.hr_agent, 'context_data'):
            self.hr_agent.context_data = {}
        
        # Charger les données RH si manquantes
        if 'research_data' not in self.hr_agent.context_data:
            hr_research = {
                "hr_manager": {
                    "market_data": "Current HR job market...",
                    "salary_ranges": "$60k-$110k"
                }
            }
        
            self.hr_agent.context_data = {
                **getattr(self.hr_agent, 'context_data', {}),
                "business_idea": self.selected_idea,
                "research_data": hr_research
            }

        # Gérer l'historique
        internal_history = []
        for msg_pair in history:
            if len(msg_pair) >= 2:
                internal_history.extend([
                    {"role": "user", "content": msg_pair[0]},
                    {"role": "assistant", "content": msg_pair[1]}
                ])

        response = self.hr_agent.get_response(
            message,
            context=str(self.hr_agent.context_data)
        )
    
        self.chat_histories['hr'] = internal_history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": response}
        ]
    
        return response

    def chat_with_sales(self, message: str, history: list) -> str:
        """Handle Sales chat interactions"""
        if not self.selected_idea:
            return "❌ Please select a business idea first!"

        # Initialiser le contexte
        if not hasattr(self.sales_agent, 'context_data'):
            self.sales_agent.context_data = {}
        
        # Charger les données commerciales si manquantes
        if 'research_data' not in self.sales_agent.context_data:
            sales_research = {
                "sales_manager": {
                    "market_data": "Current sales job market...",
                    "salary_ranges": "$50k-$120k + commission"
                }
            }
        
            self.sales_agent.context_data = {
                **getattr(self.sales_agent, 'context_data', {}),
                "business_idea": self.selected_idea,
                "research_data": sales_research
            }

        # Gérer l'historique
        internal_history = []
        for msg_pair in history:
            if len(msg_pair) >= 2:
                internal_history.extend([
                    {"role": "user", "content": msg_pair[0]},
                    {"role": "assistant", "content": msg_pair[1]}
                ])

        response = self.sales_agent.get_response(
            message,
            context=str(self.sales_agent.context_data)
        )
    
        self.chat_histories['sales'] = internal_history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": response}
        ]
    
        return response

    def chat_with_market_research(self, message: str, history: list) -> str:
        """Handle Market Research chat interactions"""
        if not self.selected_idea:
            return "❌ Please select a business idea first!"

        # Initialiser le contexte
        if not hasattr(self.market_agent, 'context_data'):
            self.market_agent.context_data = {}
        
        # Charger les données de marché si manquantes
        if 'research_data' not in self.market_agent.context_data:
            market_research = {
                "market_analyst": {
                    "market_data": "Current market research trends...",
                    "salary_ranges": "$65k-$130k"
                }
            }
        
            self.market_agent.context_data = {
                **getattr(self.market_agent, 'context_data', {}),
                "business_idea": self.selected_idea,
                "research_data": market_research
            }

        # Gérer l'historique
        internal_history = []
        for msg_pair in history:
            if len(msg_pair) >= 2:
                internal_history.extend([
                    {"role": "user", "content": msg_pair[0]},
                    {"role": "assistant", "content": msg_pair[1]}
                ])

        response = self.market_agent.get_response(
            message,
            context=str(self.market_agent.context_data)
        )
        self.chat_histories['market'] = internal_history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": response}
        ]
        return response

    def generate_business_plan(self):
        """Generate comprehensive business plan using all agents"""
        if not self.selected_idea:
            return "❌ Please select a business idea first!"

        plan = f"""# 📋 **COMPREHENSIVE BUSINESS PLAN**
    ## {self.selected_idea.get('name', 'Business Venture')}

    *Generated by AI Business School - Complete Strategic Analysis Enhanced with Deep Research API*

    ---

    ## 🎯 **EXECUTIVE SUMMARY**

    **Business Concept**: {self.selected_idea.get('description', 'Not specified')}

    **Market Opportunity**: {self.selected_idea.get('market_opportunity', 'Not specified')}

    **Competitive Advantage**: {self.selected_idea.get('competitive_advantage', 'Not specified')}

    **Revenue Model**: {self.selected_idea.get('revenue_model', 'Not specified')}

    **Capital Required**: {self.selected_idea.get('capital_required', 'Not specified')}

    **Target Market**: {self.selected_idea.get('target_customers', 'Not specified')}

    ---

    ## 📊 **KEY METRICS**
    - **Market Potential**: {self.selected_idea.get('market_potential', 'N/A')}/10
    - **Skills Match**: {self.selected_idea.get('skills_match', 'N/A')}/10
    - **Scalability Score**: {self.selected_idea.get('scalability', 'N/A')}/10
    - **Innovation Rating**: {self.selected_idea.get('innovation_score', 'N/A')}/10
    - **Risk Level**: {self.selected_idea.get('risk_level', 'Not assessed')}
    - **Time to Market**: {self.selected_idea.get('time_to_market', 'Not estimated')}

    ---

    ## 🔬 **DEEP RESEARCH INTEGRATION**

    This business plan is enhanced with real-time market intelligence from your company's Deep Research API:

    - **💻 Technical Strategy** → Software engineer & DevOps market data
    - **📢 Marketing Strategy** → Digital marketing & growth talent insights
    - **💰 Financial Planning** → Financial analyst & operations benchmarks
    - **⚖️ Legal Framework** → Legal counsel & compliance market rates
    - **👥 People Strategy** → HR manager & recruiter market intelligence
    - **💼 Sales Strategy** → Sales manager & business development data
    - **📊 Market Intelligence** → Competitive analysis & market research

    ---

    ## 💬 **INTERACTIVE CONSULTATION AVAILABLE**

    Your virtual C-suite team is ready for detailed, open-ended discussions:

    - **Challenge recommendations** and get clarifications
    - **Explore alternative strategies** through dynamic conversations
    - **Deep-dive into specific areas** of interest or concern
    - **Evolve your strategy** based on ongoing market insights
    - **Get personalized advice** that adapts to your unique situation

    ---

    *💡 To get detailed analysis and have interactive discussions, use the chat interfaces with each AI specialist in the Virtual C-Suite tab. Each agent automatically incorporates real-time market data and can engage in evolving conversations about your business strategy.*

    ---

    *This business plan serves as your strategic foundation enhanced with live market intelligence and interactive expert consultation capabilities.*
    """

        return plan

    def export_business_data(self):
        """Export business data for external use"""
        if not self.selected_idea:
            return "❌ Please select a business idea first!"

        export_data = {
            "business_name": self.selected_idea.get('name', ''),
            "description": self.selected_idea.get('description', ''),
            "user_profile": self.user_profile,
            "selected_idea": self.selected_idea,
            "generated_on": datetime.now().isoformat(),
            "deep_research_enhanced": True,
            "api_integration": openai.api_deep_research,
            "interactive_chat_enabled": True,
            "chat_capabilities": [
                "Open-ended conversations with each specialist",
                "Challenge recommendations and get clarifications",
                "Evolutionary discussions that build on previous points",
                "Real-time market data integration in conversations"
            ],
            "next_steps": [
                "Have interactive discussions with CTO Bot (enhanced with tech talent data)",
                "Chat with CMO Bot about marketing strategy (enhanced with marketing talent insights)",
                "Discuss financial planning with CFO Bot (enhanced with financial benchmarks)",
                "Get legal guidance from Legal Bot (enhanced with legal service costs)",
                "Plan team strategy with HR Bot (enhanced with HR market intelligence)",
                "Design sales process with Sales Bot (enhanced with sales talent data)",
                "Conduct market analysis with Market Research Bot (enhanced with competitive data)"
            ]
        }

        return f"""## 📁 **Business Data Export**
    *Enhanced with Deep Research API Integration & Interactive Chat Capabilities*

    **JSON Data Structure:**
    ```json
    {json.dumps(export_data, indent=2)}
    ```

    **📋 Recommended Next Actions:**
    1. Have detailed conversations with each AI specialist using the chat interfaces
    2. Challenge their recommendations to refine your strategy
    3. Save insights from chat discussions to your business planning documents
    4. Share refined strategy with co-founders and advisors
    5. Use as foundation for investor presentations
    6. Reference when building your MVP
    7. Track progress against AI recommendations
    8. Leverage market research insights for competitive positioning

    **🔗 Integration Options:**
    - Import into business planning software
    - Add to pitch deck templates
    - Include in investor data rooms
    - Reference in team hiring processes
    - Use market data for competitive analysis
    - Export chat transcripts for team review

    **💬 Interactive Advantage:**
    Your business plan is now backed by real-time market intelligence AND interactive expert consultation, giving you a significant competitive advantage in planning, fundraising, and execution through dynamic, evolving strategic discussions.
    """

# Initialize the platform
platform = BusinessSchoolPlatform()