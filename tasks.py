import asyncio
from celery_worker import celery_app
#
from loader import bot
from database import db
from models.user import get_all_user_ids


@celery_app.task
def send_ad_task(ad_text: str):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_to_all_users(ad_text))

async def send_to_all_users(ad_text: str):
    user_ids = await get_all_user_ids()
    for uid in user_ids:
        try:
            await bot.send_message(uid, ad_text)
        except Exception as e:
            print(f"Error sending to {uid}: {e}")
