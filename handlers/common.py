from aiogram import types
from bot_settings import dp
from database import bad_words, hellos


async def echo_send(message: types.Message):
    text = message.text.lower()
    print(text)
    if not text:
        await message.answer('Сообщение должно содержать хотя бы одно слово.')
    elif await bad_words.find_one({'bad_word': text}):
        await message.answer('Пожалуйста, не материтесь')
    elif await hellos.find_one({'hello_word': text}):
        await message.answer('Приветик!')
    elif text == 'как дела?':
        await message.answer('Пойдет. У вас?')
    elif text == 'что делаешь?':
        await message.answer('Давайте уже к делу, пишите /help')


# Регистрация хэндлеров
def register_handlers():
    dp.register_message_handler(echo_send)