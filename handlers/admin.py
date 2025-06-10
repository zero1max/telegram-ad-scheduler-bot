from aiogram import F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from datetime import datetime
#
from loader import router_admin
from middlewares.admin_filter import AdminFilter
from tasks import send_ad_task
from models.ads import save_ad


router_admin.message.filter(AdminFilter())  

class AdStates(StatesGroup):
    waiting_for_text = State()
    waiting_for_datetime = State()

@router_admin.message(Command("reklama"))
async def ask_ad_text(message: Message, state: FSMContext):
    await message.answer("Reklama matnini yuboring:")
    await state.set_state(AdStates.waiting_for_text)

@router_admin.message(AdStates.waiting_for_text)
async def get_text(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer("Reklama yuboriladigan vaqtni yuboring (YYYY-MM-DD HH:MM):")
    await state.set_state(AdStates.waiting_for_datetime)


@router_admin.message(AdStates.waiting_for_datetime)
async def schedule_ad(message: Message, state: FSMContext):
    data = await state.get_data()
    ad_text = data['text']
    send_time = datetime.strptime(message.text, "%Y-%m-%d %H:%M") # type: ignore

    await save_ad(ad_text, send_time)

    # Celeryga yuborish
    send_ad_task.apply_async(args=[ad_text], eta=send_time) # type: ignore

    await message.answer("Reklama belgilangan vaqtda yuboriladi.")
    await state.clear()
