from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Notification
from schemas import NotificationCreate

router = APIRouter()

@router.post("/")
def create_notification(notification: NotificationCreate, db: Session = Depends(get_db)):
    notification_data = notification.dict()
    print("NOTIFIC ATION DATA IS ", notification_data)
    new_notification = Notification(**notification_data)
    db.add(new_notification)
    db.commit()
    db.refresh(new_notification)
    return notification

@router.get("/")
def get_notifications(db: Session = Depends(get_db)):
    return db.query(Notification).all()

@router.get("/{user_id}")
def get_notification_by_user_id(user_id: int, db: Session = Depends(get_db)):
    return (
        db.query(Notification)
        .filter(Notification.user_id == user_id)
        .filter(Notification.is_read == False)
        .all()
    )

@router.put("/{notification_id}")
def mark_notification_as_read(notification_id: int, db: Session = Depends(get_db)):
    notification = db.query(Notification).get(notification_id)
    if notification:
        notification.is_read = True
        db.commit()
        return {"message": "Notification marked as read"}
    return {"message": "Notification not found"}
