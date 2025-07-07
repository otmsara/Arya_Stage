from fastapi import FastAPI
from .api.endpoints import ideas, strategies, chat
from .config import Config

app = FastAPI(
    title="AI Business School API",
    description="API for AI-powered business strategy agents",
    version="1.0.0",
    openapi_url=f"{Config.API_PREFIX}/openapi.json"
)

app.include_router(ideas.router, prefix=Config.API_PREFIX)
app.include_router(strategies.router, prefix=Config.API_PREFIX)
app.include_router(chat.router, prefix=Config.API_PREFIX)