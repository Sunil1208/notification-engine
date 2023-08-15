
# Notification Engine

The Notification Engine is a backend system built using FastAPI that allows firing notifications to users and provides real-time notifications through a WebSocket endpoint.

## Objective

The objective of the Notification Engine is to provide a robust and efficient notification system that allows users to receive important alerts and recommendations. The system should be able to store notifications in a database for future retrieval and provide real-time notifications through a WebSocket endpoint. Additionally, the system should have a feature to mark notifications as read.

## Approach

The Notification Engine is built using the following approach:
1. Backend Framework: The system is built using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python.
2. Database: The system uses a SQLite database to store notifications. The database is created and managed using SQLAlchemy, an Object-Relational Mapping (ORM) library for Python.
3. API Endpoints: The system provides several API endpoints to interact with the notification system. These endpoints include creating a notification, retrieving all notifications, retrieving notifications by user ID, and marking a notification as read.
4. WebSocket Endpoint: The system provides a WebSocket endpoint where users can receive real-time notifications. The WebSocket connection is established using the websockets library.
5. Mock Events: To simulate events that trigger notifications, a mock_events.py script is provided. This script generates mock events such as receiving a new message, subscription expiry, and profile setup completion.

## Features

The Notification Engine provides the following features:
- __Notification Creation__: Users can create notifications with a title, description, and identifier to categorize them. Notifications can be fired from anywhere in the codebase.
- __Notification Storage__: Notifications are stored in a database for future retrieval. The system uses a SQLite database by default, but it can be configured to use a different database if needed.
- __Real-time Notifications__: Users can receive real-time notifications through a WebSocket endpoint. The system sends notifications to the connected WebSocket clients whenever a new notification is created.
- __Notification Retrieval__: Users can retrieve all notifications or filter notifications by user ID. Notifications can be retrieved using the corresponding API endpoints.
- __Mark as Read__: Users can mark notifications as read using the API endpoint. Marking a notification as read changes its status to "read" and allows users to keep track of which notifications they have already seen.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

## Prerequisites

Make sure you have the following software installed:

Python (version 3.6 or higher)
Django (version 4.2.3)
Virtual environment tool (e.g., virtualenv, conda)



## Installation

Clone the repository:

```bash
git clone https://github.com/Sunil1208/notification-engine
```

Navigate to the project directory:
```bash
cd notification-engine
```

Create and active a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```
    
Install the project dependencies

```bash
pip install -r requirements.txt
```

The system uses a SQLite database by default. If you want to use a different database, update the `SQLALCHEMY_DATABASE_URL` in the `database.py` file.

## Usage

1. Start the server:

```bash
   uvicorn main:app --reload
```

2. The server will start running at http://localhost:8000.

3. Use the following endpoints to interact with the notification system:

- Create a notification: POST /notifications/
    - Request body:

```bash
{
    "title": "New Message Received",
    "description": "This is a new message from John Doe",
    "identifier": "MESSAGE",
    "user_id": 123
}
```
- Get all notifications: GET `/notifications/`

- Get notifications by user ID: GET `/notifications/{user_id}`

- Mark a notification as read: PUT `/notifications/{notification_id}`

4. To receive real-time notifications, connect to the WebSocket endpoint:

```
ws://localhost:8000/notifications/ws/{user_id}
```
- Replace `{user_id}` with the actual user ID.

5. To generate mock events that trigger notifications, run the mock_events.py script:

```python mock_events.py```

- This script simulates events such as receiving a new message, subscription expiry, and profile setup completion.

6. To receive/see real-time notifications, you can run the websocket_client.py script:
- In a different tab run the websocket_client.py script by running the following command:
```bash
python websocket_client.py
```
- The websocket_client.py script establishes a WebSocket connection with the notification system's WebSocket endpoint.
- It continuously listens for incoming notifications from the server and prints them when received.
- The script parses the received JSON messages and allows further processing of the notification data in Python.

7. If you want to access the notification via web-browser console, you can use the following code in the console of the browser:
- Replace the user_id with the actual user_id.
```bash
const user_id = 123;
const websocketURL = `ws://localhost:8000/notifications/ws/${user_id}`;

const ws = new WebSocket(websocketURL);

ws.addEventListener('open', () => {
  console.log(`Connected to WebSocket server for user ${user_id}`);
});

ws.addEventListener('message', (event) => {
  console.log(`Notification received from user ${user_id}`);
  
  try {
    const json_data = JSON.parse(event.data);
    console.log('Notification data is:', json_data);
  } catch (error) {
    console.error('Error decoding JSON:', error.message);
  }
});

ws.addEventListener('close', () => {
  console.log('WebSocket connection closed');
});

```
## Postman Collection

To access, test and for the reference of the api's, the following published collection can be used.

https://documenter.getpostman.com/view/10156058/2s9Xy6p9gS