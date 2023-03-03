import logging

from aiogram.utils import executor
from bot_settings import dp
from handlers import commands, common
logging.basicConfig(level=logging.INFO)


# Первый запуск бота
async def startup(_):
    print("Бот успешно запущен")


if __name__ == "__main__":
    try:
        commands.register_handlers()
        common.register_handlers()
        # skip_updates = True, чтоб не засыпало сообщениями, после выключения бота
        executor.start_polling(dp, skip_updates=True, on_startup=startup)
    except:
        print('У меня какие-то проблемы, простите')
        exit()