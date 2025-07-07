from typing import Dict, List
from .agents import (
    IdeaScoutAgent, CTOAgent, CMOAgent,
    CFOAgent, LegalAgent, HRAgent,
    SalesAgent, MarketResearchAgent
)

class BusinessSchoolPlatform:
    """Main platform class to manage agents and state"""
    def __init__(self):
        self.agents = {
            'idea_scout': IdeaScoutAgent(),
            'cto': CTOAgent(),
            'cmo': CMOAgent(),
            'cfo': CFOAgent(),
            'legal': LegalAgent(),
            'hr': HRAgent(),
            'sales': SalesAgent(),
            'market': MarketResearchAgent()
        }
        self.user_profile = {}
        self.selected_idea = None
        self.chat_histories = {agent: [] for agent in self.agents.keys()}
    
    def update_agent_context(self, agent_name: str, business_idea: Dict):
        """Update context for a specific agent"""
        if agent_name in self.agents:
            self.agents[agent_name].context_data['business_idea'] = business_idea