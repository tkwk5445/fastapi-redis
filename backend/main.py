import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import aioredis

app = FastAPI()

# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Redis 클라이언트
redis = None

class KeyValue(BaseModel):
    key: str
    value: str

@app.on_event("startup")
async def startup_event():
    global redis
    redis_endpoint = os.getenv("REDIS_ENDPOINT")
    if not redis_endpoint:
        raise ValueError("REDIS_ENDPOINT environment variable is not set.")
    try:
        redis = await aioredis.from_url(f"redis://{redis_endpoint}", decode_responses=True)
        await redis.ping()  # Redis 연결 테스트
    except Exception as e:
        print(f"Failed to connect to Redis: {e}")
        raise

@app.on_event("shutdown")
async def shutdown_event():
    if redis:
        await redis.close()

@app.post("/set")
async def set_key_value(data: KeyValue):
    await redis.setex(data.key, 60, data.value)
    return {"message": f"Key '{data.key}' set to '{data.value}' with 60 seconds TTL"}

@app.get("/get/{key}")
async def get_key_value(key: str):
    value = await redis.get(key)
    if value:
        return {"key": key, "value": value, "source": "cache"}
    return {"error": f"Key '{key}' not found in cache"}

