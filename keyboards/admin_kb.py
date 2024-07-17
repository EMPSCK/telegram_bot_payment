from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

admin_kb_button = [InlineKeyboardButton(text="Организовать рассылку", callback_data='newsletter')]
admin_kb_show_user_list_button = [InlineKeyboardButton(text="Просмотреть список пользователей", callback_data='show_user_list')]
admin_kb = InlineKeyboardMarkup(inline_keyboard=[admin_kb_button, admin_kb_show_user_list_button])

admin_back_kb_button = [InlineKeyboardButton(text="Вернуться назад", callback_data='go_back_admin')]
admin_back_kb = InlineKeyboardMarkup(inline_keyboard=[admin_back_kb_button])

confirm_newsletter_kb_button = [InlineKeyboardButton(text="Подтвердить", callback_data='confirm_newsletter')]
confirm_newsletter_kb = InlineKeyboardMarkup(inline_keyboard=[confirm_newsletter_kb_button, admin_back_kb_button])
