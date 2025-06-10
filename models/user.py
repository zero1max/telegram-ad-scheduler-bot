from database import db

async def save_user(user_id: int):
    existing = await db.users.find_one({"_id": user_id})
    if not existing:
        await db.users.insert_one({"_id": user_id})

async def get_all_user_ids():
    users = await db.users.find().to_list(length=None)
    return [user["_id"] for user in users]
