from aiogram.utils import executor
from bot_settings import dp
from handlers import client, common


# Первый запуск бота
async def startup(_):
    print("Бот успешно запущен")


if __name__ == "__main__":
    try:
        client.register_handlers()
        common.register_handlers()
        # skip_updates = True, чтоб не засыпало сообщениями, после выключения бота
        executor.start_polling(dp, skip_updates=True, on_startup=startup)
    except:
        print('У меня какие-то проблемы, простите')
        exit()