import asyncio
import logging
from aiogram.utils import executor
from bot_settings import dp
from database import client
from handlers import commands, common
from middlewares import ThrottlingMiddleware
logging.basicConfig(level=logging.INFO)


# Первый запуск бота
async def startup(_):
    print("Бот успешно запущен")


async def shutdown():
    # Закрыть сессии в Redis и MongoDB
    tasks = [dp.storage.close(), client.close()]
    await asyncio.gather(*tasks)
    print('Бот успешно выключен')


if __name__ == "__main__":
    try:
        commands.register_handlers()
        common.register_handlers()
        dp.middleware.setup(ThrottlingMiddleware(limit=0.5))
        # skip_updates = True, чтоб не засыпало сообщениями, после выключения бота
        executor.start_polling(dp, skip_updates=True, on_startup=startup, on_shutdown=shutdown)
    except:
        print('У меня какие-то проблемы, простите')
        exit()