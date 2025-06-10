from motor.motor_asyncio import AsyncIOMotorClient
#
from loader import MONGO_URI

mongo_client = AsyncIOMotorClient(MONGO_URI)
db = mongo_client["telegram_bot"]
