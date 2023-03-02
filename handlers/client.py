from aiogram import types
from bot_settings import dp


# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    try:
        await message.answer('Привет, меня зовут Сулужан, чтоб узнать о моих функциях напишите /help')
    # Если не может писать
    except:
        await message.answer('У меня какие-то проблемы, простите')


# @dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    try:
        await message.answer('*Инструкция*')
    # Если не может писать
    except:
        await message.answer('У меня какие-то проблемы, простите')


# Регистрация хэндлеров
def register_handlers():
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
