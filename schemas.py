from pydantic import BaseModel

class NotificationCreate(BaseModel):
    title: str
    description: str
    identifier: str
    user_id: int
