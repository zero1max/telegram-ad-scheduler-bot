from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

celery_app = Celery(
    "tasks",
    broker=os.getenv("REDIS_BROKER"),
    backend=os.getenv("REDIS_BROKER")
)

# Tasklarni ro'yxatga olish
import tasks  # <== bu MUHIM!
