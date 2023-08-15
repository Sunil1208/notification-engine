from sqlalchemy import Column, Integer, String, DateTime, Boolean, func
from database import Base, engine

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    identifier = Column(String, index=True)
    user_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    is_read = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)