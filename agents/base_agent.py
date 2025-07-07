import openai
import requests
from datetime import datetime
from typing import Dict, List, Tuple
import json

class AIAgent:
    """Base class for all AI agents with Deep Research integration"""
    def __init__(self, name: str, role: str, expertise: str):
        self.name = name
        self.role = role
        self.expertise = expertise
        self.model = "gpt-4o"
        self.deep_research_api = "https://your-research-api.com/deep_research"
        self.chat_history = []
        self.context_data = {}

    def configure_openai(self, api_key: str, api_base: str, api_version: str):
        openai.api_type = "azure"
        openai.api_key = api_key
        openai.api_base = api_base
        openai.api_version = api_version

    def get_response(self, prompt: str, context: str = "", chat_history: List = None) -> str:
        """Core method to get AI response"""
        messages = [
            {"role": "system", "content": f"You are {self.name}, a {self.role}. Your expertise: {self.expertise}\n\nCONTEXT:\n{context}"}
        ]
        
        if chat_history:
            messages.extend(chat_history[-10:])
            
        messages.append({"role": "user", "content": prompt})
        
        try:
            response = openai.ChatCompletion.create(
                engine=self.model,
                messages=messages,
                max_tokens=2000,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

    def get_deep_research_data(self, job_role: str, business_context: str) -> Dict:
        """Fetch market research data"""
        payload = {
            "job_posting_id": f"research_{job_role}_{datetime.now().strftime('%Y%m%d')}",
            "resume": business_context
        }
        try:
            response = requests.post(
                self.deep_research_api,
                json=payload,
                headers={'Content-Type': 'application/json'},
                timeout=15
            )
            return response.json() if response.status_code == 200 else {}
        except Exception:
            return {}
    
    def chat(self, message: str, history: List) -> Tuple[str, List]:
        """Handle interactive chat"""
        response = self.get_response(message, self._build_context(), history)
        updated_history = history + [
            {"role": "user", "content": message},
            {"role": "assistant", "content": response}
        ]
        return response, updated_history
    
    def _build_context(self) -> str:
        """Build context string from stored data"""
        context = ""
        if 'business_idea' in self.context_data:
            idea = self.context_data['business_idea']
            context += f"Business: {idea.get('name')}\nDescription: {idea.get('description')}"
        if 'research_data' in self.context_data:
            context += f"\nResearch Data: {json.dumps(self.context_data['research_data'])}"
        return context