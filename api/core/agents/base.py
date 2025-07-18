from openai import AzureOpenAI
import requests
import os
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class AIAgent:
    """Base class for all AI agents with Deep Research integration and chat capabilities"""
    def __init__(self, name: str, role: str, expertise: str):
        self.name = name
        self.role = role
        self.expertise = expertise
        
        # Configure Azure OpenAI
        self.api_type = "azure"
        self.api_key = os.getenv("AZURE_OPENAI_API_KEY")
        self.api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
        self.api_version = os.getenv("AZURE_OPENAI_API_VERSION")
        self.deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
        
        # Configure Deep Research
        self.deep_research_api = os.getenv("DEEP_RESEARCH_API_URL")
        
        # Initialize chat state
        self.chat_history: List[Dict] = []
        self.context_data: Dict = {}

        # Verify configuration
        if not all([self.api_key, self.api_base, self.api_version, self.deployment_name]):
            raise ValueError("Missing required Azure OpenAI configuration")

    def _get_openai_client(self):
        """Configure and return OpenAI client"""
        return AzureOpenAI(
            api_key=self.api_key,
            api_version=self.api_version,
            azure_endpoint=self.api_base  # Changed from base_url
        )

    def get_response(self, prompt: str, context: str = "", chat_history: Optional[List] = None) -> str:
        """Get response from Azure OpenAI"""
        try:
            client = self._get_openai_client()
            
            messages = [
                {
                    "role": "system",
                    "content": f"""You are {self.name}, a {self.role}. Your expertise is in {self.expertise}.
                    
                    BUSINESS CONTEXT:
                    {context}
                    
                    INSTRUCTIONS:
                    - Provide detailed, actionable advice based on your expertise
                    - Use current 2025 market insights and trends
                    - Be conversational and interactive - encourage follow-up questions
                    - Reference previous conversation points when relevant
                    - Challenge user assumptions when necessary to provide better guidance
                    - Ask clarifying questions to better understand their needs
                    - Provide specific examples and recommendations
                    - Consider startup constraints (budget, time, resources)
                    - When relevant, reference market research data to support recommendations
                    - Be encouraging but realistic about challenges
                    """
                }
            ]

            if chat_history:
                messages.extend(chat_history[-10:])  # Last 10 messages

            messages.append({"role": "user", "content": prompt})

            response = client.chat.completions.create(
                model=self.deployment_name,
                messages=messages,
                max_tokens=2000,
                temperature=0.7,
                top_p=0.9
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"🚨 Error connecting to AI service: {str(e)}"

    def get_deep_research_data(self, job_role: str, business_context: str) -> str:
        """Get market research data from company API"""
        try:
            payload = {
                "job_posting_id": f"ai_research_{job_role.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
                "resume": business_context
            }

            response = requests.post(
                self.deep_research_api,
                json=payload,
                headers={
                    'accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                timeout=15
            )

            if response.status_code == 200:
                return response.json()
            else:
                return f"Research data unavailable (Status: {response.status_code})"

        except Exception as e:
            return f"Research API temporarily unavailable: {str(e)}"

    def create_business_context(self, business_idea: Dict, focus_area: str) -> str:
        """Create business context for deep research API"""
        return f"""
        Business: {business_idea.get('name', 'Startup')}
        Industry: {focus_area}
        Description: {business_idea.get('description', 'Innovative startup')}
        Target Market: {business_idea.get('target_customers', 'General market')}
        Revenue Model: {business_idea.get('revenue_model', 'To be determined')}
        Stage: Early-stage startup
        Capital: {business_idea.get('capital_required', 'Seeking funding')}
        Market Opportunity: {business_idea.get('market_opportunity', 'Emerging market')}
        """

    def update_context(self, business_idea: Dict = None, research_data: str = None):
        """Update agent's context with business data and research"""
        if business_idea:
            self.context_data['business_idea'] = business_idea
        if research_data:
            self.context_data['research_data'] = research_data

    def chat(self, message: str, history: List) -> Tuple[str, List]:
        """Handle interactive chat with the agent"""
        # Create context string from stored data
        context = ""
        if 'business_idea' in self.context_data:
            idea = self.context_data['business_idea']
            context += f"""
            CURRENT BUSINESS FOCUS:
            - Business: {idea.get('name', 'Not specified')}
            - Description: {idea.get('description', 'Not specified')}
            - Target Market: {idea.get('target_customers', 'Not specified')}
            - Revenue Model: {idea.get('revenue_model', 'Not specified')}
            """

        if 'research_data' in self.context_data:
            context += f"\n\nMARKET RESEARCH DATA:\n{self.context_data['research_data']}"

        # Get response
        response = self.get_response(message, context, history)

        # Update history
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": response})

        return response, history