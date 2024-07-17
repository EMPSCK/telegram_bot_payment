import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import hello_stage
from handlers import payment
from handlers import admin


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(hello_stage.router)
    dp.include_router(payment.router)
    dp.include_router(admin.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
