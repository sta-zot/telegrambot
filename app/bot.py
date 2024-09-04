import asyncio
from aiogram import Dispatcher, Bot
from aiogram.methods import DeleteWebhook
from settings.configuration import config
from app.commands import general_commands
from app.handlers import router as handler_router


bot = Bot(config.bot_api_key)
dp = Dispatcher()
dp.include_router(handler_router)


# Функция для запуска бота
async def start_bot(bot: Bot = bot):
    await bot(DeleteWebhook(drop_pending_updates=True))
    await bot.set_my_commands(general_commands)
    await dp.start_polling(bot)


# Функция для остановки бота
async def stop_bot(bot: Bot = bot):
    await dp.stop_polling()

if __name__ == "__main__":
    asyncio.run(start_bot())