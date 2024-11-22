Redis Caching Example
Introduction
This project demonstrates a simple Redis caching application using:

Frontend: Nginx serving an HTML/JavaScript-based interface.
Backend: FastAPI providing REST API endpoints.
Cache Layer: AWS ElastiCache (Redis) for key/value storage with TTL (Time-To-Live).
Features
Store key-value pairs in Redis with a TTL of 60 seconds.
Retrieve values by key from Redis.
Simple UI to interact with the application.
Uses Docker Compose for easy deployment.
Architecture
plaintext
코드 복사
USER
 │
 └──> Frontend (Nginx, HTML/JS)
         │
         └──> Backend (FastAPI)
                  │
                  └──> AWS ElastiCache (Redis)
Frontend: Collects user input and sends API requests to the backend.
Backend: Handles /set and /get/{key} API endpoints.
Redis: Stores the key-value pairs with a TTL of 60 seconds.
API Endpoints
1. POST /set
Stores a key-value pair in Redis with a TTL of 60 seconds.

Request:
json
코드 복사
{
  "key": "test",
  "value": "12345"
}
Response:
json
코드 복사
{
  "message": "Key 'test' set to '12345' with 60 seconds TTL"
}
2. GET /get/{key}
Retrieves the value of a key from Redis.

Request:
sql
코드 복사
GET /get/test
Response (if key exists):
json
코드 복사
{
  "key": "test",
  "value": "12345",
  "source": "cache"
}
Response (if key does not exist):
json
코드 복사
{
  "error": "Key 'test' not found in cache"
}
Setup Instructions
Prerequisites
Docker & Docker Compose installed.
AWS ElastiCache (Redis) cluster set up.
Steps
Clone the repository:

bash
코드 복사
git clone https://github.com/<your-repo-name>.git
cd <your-repo-name>
Set up environment variables: Create a .env file in the root directory and add your Redis endpoint:

env
코드 복사
REDIS_ENDPOINT=master.board-redis-cluster.ozdo2v.apn2.cache.amazonaws.com:6582
Start the application:

bash
코드 복사
docker-compose up --build
Access the application: Open your browser and navigate to:

arduino
코드 복사
http://<your-instance-ip>:8080
Project Structure
plaintext
코드 복사
.
├── frontend/
│   ├── Dockerfile       # Frontend Dockerfile
│   └── index.html       # HTML/JS for the user interface
├── backend/
│   ├── Dockerfile       # Backend Dockerfile
│   └── main.py          # FastAPI application
├── docker-compose.yml   # Docker Compose configuration
└── README.md            # Project documentation
How It Works
The frontend collects user input (key and value) via a simple web form.
API requests are sent to the backend to either:
Store the key-value pair in Redis (POST /set).
Retrieve the value for a specific key (GET /get/{key}).
The backend interacts with AWS ElastiCache to handle data storage and retrieval.
Tech Stack
Frontend: HTML, JavaScript, Nginx.
Backend: FastAPI (Python).
Cache Layer: AWS ElastiCache (Redis).
Deployment: Docker Compose.
