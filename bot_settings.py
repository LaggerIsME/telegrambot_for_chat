import json
from aiogram import Bot
from aiogram.dispatcher import Dispatcher


# Получить токен бота
def get_token(path: str = 'token.json'):
    try:
        # Открыть файл с токеном
        with open(path, 'r') as read_file:
            data = json.load(read_file)
        # Достать его из словаря
        token = data['token']
        return token
    except:
        print("Неправильно указан путь к файлу с токеном, либо сам файл неправильного формата")
        return None


# Настройки бота
token = get_token()
# Создание бота
bot = Bot(token=token)
# Обрабатыватель сообщений Telegram
dp = Dispatcher(bot)