from fastapi import FastAPI, WebSocket
from websocket import websocket_handler

app = FastAPI()

# Import and register the notification routes
from notifications import router as notification_router

app.include_router(notification_router, prefix="/notifications", tags=["notifications"])

@app.websocket("/notifications/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await websocket.accept()
    await websocket_handler(websocket, user_id=user_id)

# start_server = websockets.serve(websocket_handler, "localhost", 8765)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)