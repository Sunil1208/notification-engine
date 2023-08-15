import asyncio
import websockets
import json

async def websocket_client():
    user_id = 123 # update the user_id for which you want to receive the notification
    async with websockets.connect(f"ws://localhost:8000/notifications/ws/{user_id}") as ws:
        while True:
            message = await ws.recv()
            print(f"Notification received from user {user_id}")
            # Log the received raw message
            # print(f"Received raw message: {message}")

            try:
                # Parse the JSON message
                json_data = json.loads(message)
                # Now you can work with the parsed JSON data
                print("Notification data is :  ", json_data)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")

# Run the WebSocket client
asyncio.get_event_loop().run_until_complete(websocket_client())
