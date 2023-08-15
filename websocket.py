import asyncio
import json
from notifications import get_notifications, get_notification_by_user_id
from database import get_db
from json_encoder import NotificationEncoder

async def websocket_handler(websocket, user_id):
    db = next(get_db())
    while True:
        user_notifications = get_notification_by_user_id(user_id, db)
        serialized_notifications = json.dumps(user_notifications, cls=NotificationEncoder)
        await websocket.send_json(serialized_notifications)

        # Wait for a certain interval before sending the next update
        await asyncio.sleep(10)
