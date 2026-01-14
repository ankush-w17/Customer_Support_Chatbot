from motor.motor_asyncio import AsyncIOMotorClient
from app.config import MONGODB_URL, DB_NAME

class MongoDB:
    client: AsyncIOMotorClient = None
    db = None

    @classmethod
    async def connect(cls):
        cls.client = AsyncIOMotorClient(MONGODB_URL)
        cls.db = cls.client[DB_NAME]
        print(f"Connected to MongoDB: {DB_NAME}")

    @classmethod
    async def close(cls):
        if cls.client:
            cls.client.close()
            print("MongoDB connection closed.")

mongo_db = MongoDB()
