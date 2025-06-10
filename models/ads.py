from database import db
from datetime import datetime

async def save_ad(text: str, send_time: datetime):
    await db.ads.insert_one({
        "text": text,
        "send_time": send_time,
        "status": "scheduled"
    })
