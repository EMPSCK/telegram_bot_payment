import asyncio
from datetime import datetime, timedelta
from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram import types
from queries import change_user_status_query
import config


router = Router()

@router.callback_query(F.data == 'widget_for_payment')
async def one_more_time(callback: types.CallbackQuery):
    PRICE = types.LabeledPrice(label='Доступ', amount=500 * 100)
    inv = await callback.message.bot.send_invoice(callback.message.chat.id,
                                   title="Активация доступа к продукту",
                                   description="Счет действителен 10 минут, через минуту сообщение исчезнет",
                                   provider_token=config.SBER_TOKEN,
                                   currency="rub",
                                   is_flexible=False,
                                   prices=[PRICE],
                                   start_parameter="one-month-subscription",
                                   payload="test-invoice-payload",)

    await asyncio.sleep(60)
    await inv.delete()


# pre checkout  (must be answered in 10 seconds)
@router.pre_checkout_query(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await pre_checkout_q.bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


# successful payment
@router.message(F.successful_payment)
async def successful_payment(message: types.Message):
    await change_user_status_query.change_user_status(message.from_user.id)
    expire_date = datetime.now() + timedelta(days=1)
    link = await message.bot.create_chat_invite_link(config.CHAT_CHANNEL_ID, member_limit=1, expire_date=datetime.timestamp(expire_date))
    await message.answer('🗓Благодарим за покупку!'+ '\nтексттексттексттексттексттексттексттексттекст'+ f"\n\n<b>Ссылка(1 инвайт/24 часа): {link.invite_link}</b>", parse_mode=ParseMode.HTML)
