from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from ai_for_chatting.ai_config import ReplicaGenerator
from database import redis
import os

# Настройки бота
BOT_TOKEN = os.environ.get('BOT_TOKEN')
# Создание бота
bot = Bot(token=BOT_TOKEN)
# Обрабатыватель сообщений Telegram
dp = Dispatcher(bot, storage=redis)
# Генератор ответов
generator = ReplicaGenerator()
