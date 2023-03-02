from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from bot_settings import dp
from keyboards import kb_client
from database import anecdotes


# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    try:
        await message.answer('Привет, меня зовут Сулужан, чтоб узнать о моих функциях напишите /help', reply_markup=kb_client)
    # Если не может писать
    except:
        await message.answer('У меня какие-то проблемы, простите')


# @dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    try:
        await message.answer('*Инструкция*', reply_markup=kb_client)
    # Если не может писать
    except:
        await message.answer('У меня какие-то проблемы, простите')


async def command_anecdote(message: types.Message):
    try:
        # Вытащить случайной анекдот
        anecdote = await anecdotes.aggregate([{'$sample': {'size': 1}}]).next()
        await message.answer("Анекдот про Линукс:\n\n" + anecdote['anecdote'])
        # Если не может писать
    except:
        await message.answer('У меня какие-то проблемы, простите')


# Регистрация хэндлеров
def register_handlers():
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(command_anecdote, commands=['anecdote'])
