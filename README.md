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
