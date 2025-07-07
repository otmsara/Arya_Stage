import os
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Config(BaseSettings):
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    OPENAI_API_BASE: str = os.getenv("OPENAI_API_BASE")
    OPENAI_API_VERSION: str = "2024-08-01-preview"
    RESEARCH_API_URL: str = os.getenv("RESEARCH_API_URL")
    API_PREFIX: str = "/api/v1"
    CORS_ORIGINS: list = ["*"]

    class Config:
        env_file = ".env"