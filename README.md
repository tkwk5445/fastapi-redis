
# **Redis Caching Example**

## **Introduction**
This project demonstrates a simple **Redis caching application** using:
- **Frontend**: Nginx serving an HTML/JavaScript-based interface.
- **Backend**: FastAPI providing REST API endpoints.
- **Cache Layer**: AWS ElastiCache (Redis) for key/value storage with TTL (Time-To-Live).

### **Features**
- Store key-value pairs in Redis with a TTL of 60 seconds.
- Retrieve values by key from Redis.
- Simple UI to interact with the application.
- Uses Docker Compose for easy deployment.

---

## **Architecture**
```plaintext
USER
 │
 └──> Frontend (Nginx, HTML/JS)
         │
         └──> Backend (FastAPI)
                  │
                  └──> AWS ElastiCache (Redis)
```

- **Frontend**: Collects user input and sends API requests to the backend.
- **Backend**: Handles `/set` and `/get/{key}` API endpoints.
- **Redis**: Stores the key-value pairs with a TTL of 60 seconds.

---

## **API Endpoints**

### **1. POST `/set`**
Stores a key-value pair in Redis with a TTL of 60 seconds.

![image](https://github.com/user-attachments/assets/af3251b5-aa08-4808-9d20-76dfc4be6579)

- **Request**:
  ```json
  {
    "key": "test",
    "value": "12345"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Key 'test' set to '12345' with 60 seconds TTL"
  }
  ```

---

### **2. GET `/get/{key}`**
Retrieves the value of a key from Redis.
![image](https://github.com/user-attachments/assets/8388b2af-ea39-4f59-8af0-efcade4ef94c)


- **Request**:
  ```
  GET /get/test
  ```
- **Response (if key exists)**:
  ```json
  {
    "key": "test",
    "value": "12345",
    "source": "cache"
  }
  ```
- **Response (if key does not exist)**:
  ```json
  {
    "error": "Key 'test' not found in cache"
  }
  ```

---

## **Setup Instructions**

### **Prerequisites**
- Docker & Docker Compose installed.
- AWS ElastiCache (Redis) cluster set up.

### **Steps**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. **Set up environment variables**:
   Create a `.env` file in the root directory and add your Redis endpoint:
   ```env
   REDIS_ENDPOINT=master.board-redis-cluster.ozdo2v.apn2.cache.amazonaws.com:6582
   ```

3. **Start the application**:
   ```bash
   docker-compose up --build
   ```

4. **Access the application**:
   Open your browser and navigate to:
   ```
   http://<your-instance-ip>:8080
   ```

---

## **Project Structure**
```plaintext
.
├── frontend/
│   ├── Dockerfile       # Frontend Dockerfile
│   └── index.html       # HTML/JS for the user interface
├── backend/
│   ├── Dockerfile       # Backend Dockerfile
│   └── main.py          # FastAPI application
├── docker-compose.yml   # Docker Compose configuration
└── README.md            # Project documentation
```

---

## **How It Works**
1. The **frontend** collects user input (key and value) via a simple web form.
2. API requests are sent to the **backend** to either:
   - Store the key-value pair in Redis (`POST /set`).
   - Retrieve the value for a specific key (`GET /get/{key}`).
3. The **backend** interacts with AWS ElastiCache to handle data storage and retrieval.

---

## **Tech Stack**
- **Frontend**: HTML, JavaScript, Nginx.
- **Backend**: FastAPI (Python).
- **Cache Layer**: AWS ElastiCache (Redis).
- **Deployment**: Docker Compose.
