from fastapi import FastAPI
from api.endpoints.router import router

app = FastAPI()
app.include_router(router)

# Add root endpoint
@app.get("/")
async def root():
    return {
        "message": "AI Business School API",
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000)