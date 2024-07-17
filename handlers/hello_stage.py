from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from queries import create_user_query
from queries import is_admin_query
from keyboards import widget_for_payment_kb
from keyboards import admin_kb

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await create_user_query.create_user(message.from_user.id, message.from_user.username)
    user_status = await is_admin_query.is_admin(message.from_user.id)
    if user_status == '2':
        await message.answer(f"👋Привет, Админ ..........", reply_markup=admin_kb.admin_kb)
    else:
        await message.answer(f"👋Привет, ..........", reply_markup=widget_for_payment_kb.widget_for_payment_kb)

