from json import JSONEncoder
from datetime import datetime
from models import Notification

class NotificationEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Notification):
            return {
                "id": obj.id,
                "title": obj.title,
                "description": obj.description,
                "identifier": obj.identifier,
                "created_at": obj.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "updated_at": obj.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
                "is_read": obj.is_read
            }
        elif isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        return super().default(obj)
