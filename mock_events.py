import asyncio
from datetime import datetime, timedelta
from database import get_db
from notifications import create_notification
from schemas import NotificationCreate

async def generate_mock_events():
    db = next(get_db())
    await asyncio.sleep(5)  # Simulating a delay before generating events

    # Generate a mock event for a new message received
    message_content = "This is a new message from John Doe"
    create_notification(NotificationCreate(
        title="New Message Received",
        description=message_content,
        identifier="MESSAGE",
        user_id=123  # Replace with the actual user ID
    ), db=db)

    await asyncio.sleep(5)

    # Generate a mock event for subscription expiry
    expiry_date = datetime.now() + timedelta(days=7)  # Assuming subscription expires in 7 days
    expiry_description = f"Your subscription will expire on {expiry_date.strftime('%Y-%m-%d')}"
    create_notification(NotificationCreate(
        title="Subscription Expiring Soon",
        description=expiry_description,
        identifier="SUBSCRIPTION_EXPIRY",
        user_id=123  # Replace with the actual user ID
    ), db=db)

    await asyncio.sleep(5)

    # Generate a mock event for profile setup completion
    create_notification(NotificationCreate(
        title="Profile Setup Complete",
        description="Congratulations! You have completed your profile setup",
        identifier="PROFILE_SETUP",
        user_id=123  # Replace with the actual user ID
    ), db=db)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(generate_mock_events())
