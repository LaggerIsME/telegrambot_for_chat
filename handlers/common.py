from aiogram import types
from bot_settings import dp
from database import bad_words, hellos


async def echo_send(message: types.Message):
    text = message.text.lower()
    text_split = text.split()
    if message.chat.type == types.ChatType.PRIVATE:
        for i in text_split:
            if not i:
                await message.answer('Сообщение должно содержать хотя бы одно слово.')
            elif await bad_words.find_one({'bad_word': i}):
                await message.answer('Пожалуйста, не материтесь')
                # Удалить сообщение с матом
                await message.delete()
            elif await hellos.find_one({'hello_word': i}):
                await message.answer('Приветик!')
        if text == 'как дела?':
            await message.answer('Пойдет. У вас?')
        elif text == 'что делаешь?':
            await message.answer('Давайте уже к делу, пишите /help')


# Регистрация хэндлеров
def register_handlers():
    dp.register_message_handler(echo_send)