from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from ...dependencies import get_platform

router = APIRouter()

@router.websocket("/{agent_type}")
async def websocket_chat(
    websocket: WebSocket,
    agent_type: str,
    platform = Depends(get_platform)
):
    """WebSocket endpoint for interactive chat"""
    if agent_type not in platform.agents:
        await websocket.close(code=1008, reason="Invalid agent type")
        return

    agent = platform.agents[agent_type]
    await websocket.accept()
    
    try:
        while True:
            message = await websocket.receive_text()
            response, _ = agent.chat(message, platform.chat_histories[agent_type])
            await websocket.send_text(response)
    except WebSocketDisconnect:
        print("Client disconnected")