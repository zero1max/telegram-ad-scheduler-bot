from aiogram import F
from aiogram.filters import CommandStart
from aiogram.types import Message
#
from loader import router_user
from models.user import save_user


@router_user.message(CommandStart())
async def start_handler(message: Message):
    await save_user(message.from_user.id) # type: ignore
    await message.answer("Assalomu alaykum! Reklama xabarlari shu yerga yuboriladi.")
