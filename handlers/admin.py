from aiogram import Router, F
from aiogram import types
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message
from keyboards import admin_kb
from queries import users_tg_id_query
from aiogram.enums import ParseMode
from queries import show_user_list_query
from aiogram.enums import ParseMode
from queries import change_active_user_query
router = Router()


class Newsletter(StatesGroup):
    newsletter_text = State()
    text = ''


@router.callback_query(F.data == 'go_back_admin')
async def go_back_admin(callback: types.CallbackQuery):
    await callback.message.edit_text(f"👋Привет, Админ ..........", reply_markup = admin_kb.admin_kb)


@router.callback_query(F.data == 'newsletter')
async def newsletter_admin(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_text('Отправьте сообщение:', reply_markup=admin_kb.admin_back_kb)
    await state.set_state(Newsletter.newsletter_text)


@router.message(Newsletter.newsletter_text)
async def ans_newsletter(message: Message):
    newsletter_text = message.text
    Newsletter.text = message.text
    await message.answer(f'<b>Текст рассылки:</b>\n\n{newsletter_text}\n\n<b>Подтвердить отправку?</b>', parse_mode=ParseMode.HTML, reply_markup=admin_kb.confirm_newsletter_kb)


@router.callback_query(F.data == 'confirm_newsletter')
async def go_back_admin(callback: types.CallbackQuery):
    newsletter_text = Newsletter.text
    users = await users_tg_id_query.get_users_tg_id()
    for user in users:
        try:
            await callback.message.bot.send_message(user[0], text=newsletter_text)
        except:
            await change_active_user_query.change_status(user[0])
    await callback.message.answer('✅Рассылка проведена успешно!', reply_markup=admin_kb.admin_back_kb)


@router.callback_query(F.data == 'show_user_list')
async def go_back_admin(callback: types.CallbackQuery):
    list_users = ['; '.join(map(str, list(user))) for user in show_user_list_query.get_user_list()]
    s = '\n'.join(list_users)
    active_num = sum(int(i[-1]) for i in list_users)
    await callback.message.edit_text(f'<b>Всего пользователей: {len(list_users)}\nАктивных: {active_num}\nНеактивных: {len(list_users) - active_num}</b>\n\n<b>id; tg_id; username; status; active</b>\n{s}', reply_markup=admin_kb.admin_back_kb, parse_mode=ParseMode.HTML)


