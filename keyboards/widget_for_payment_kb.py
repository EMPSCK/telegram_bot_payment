from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

widget_for_payment_button = [InlineKeyboardButton(text="Отправить виджет для оплаты", callback_data='widget_for_payment')]
widget_for_payment_button_admin = [InlineKeyboardButton(text="Написать администратору", url='https://t.me/EmpiricalSkeptic')]
widget_for_payment_kb = InlineKeyboardMarkup(inline_keyboard=[widget_for_payment_button, widget_for_payment_button_admin])

