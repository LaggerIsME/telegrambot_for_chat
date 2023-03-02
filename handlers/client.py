from aiogram import types
from aiogram.dispatcher.filters import Command

from bot_settings import dp
from filters import IsChatAdmin
from keyboards import kb_client


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

# async def command_give_nickname(message: types.Message):
#     try:


# Регистрация хэндлеров
def register_handlers():
    dp.register_message_handler(command_start, Command('start'), IsChatAdmin('can_restrict_members'))
    dp.register_message_handler(command_help, Command('help'), IsChatAdmin('can_restrict_members'))
