import asyncio
import logging
import os
from aiogram.utils.executor import start_webhook
from ai_for_chatting import main
from bot_settings import dp, generator, public_url, token, bot
from database import client
from handlers import commands, common
from keyboards.buttons import set_commands
from middlewares import ThrottlingMiddleware

# Роут, который будет принимать данные
WEBHOOK_PATH = f"/bot/{token}"
# Путь до данного роута в публичной сети
WEBHOOK_URL = public_url + WEBHOOK_PATH
# Расположение самого хоста в docker
WEBAPP_HOST = os.getenv('WEBAPP_HOST')
# Расположение самого порта в docker
WEBAPP_PORT = os.getenv('WEBAPP_PORT')

# Настройки бота
logging.basicConfig(level=logging.INFO)


async def on_startup(dp):
    # Подключение вебхуков
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(
            url=WEBHOOK_URL
        )
    # Искусственный интеллект
    await set_commands()
    await main(generator)


# На выключение сервера
async def on_shutdown(dp):
    tasks = [dp.storage.close(), client.close()]
    await asyncio.gather(*tasks)
    await bot.session.close()


if __name__ == "__main__":
    try:
        commands.register_handlers()
        common.register_handlers()
        dp.middleware.setup(ThrottlingMiddleware(limit=0.5))
        start_webhook(dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,)
        # skip_updates = True, чтоб не засыпало сообщениями, после выключения бота
    except:
        print('У меня какие-то проблемы, простите')
        exit()