import asyncio
import io
from aiogram import types
from bot_settings import dp, bot
from database import bad_words, hellos, gifs


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
        elif text in ['сулу', 'сулужан']:
            await message.answer('Да?')


# Нужен чел с премиум, пока проверить нереально
# Удаляет сообщение и дает бан тем, кто пишет от канала
async def delete_channel_messages(message: types.Message):
    if message.chat.type == types.ChatType.CHANNEL:
        await message.delete()
        chat_id = message.chat.id
        await message.bot.restrict_chat_member(chat_id, message.from_user.id, can_send_messages=False)


# Приветствие для нового пользователя
async def welcome(message: types.Message):
    gif_doc = await gifs.find_one({'name': 'mygif'})
    gif_data = gif_doc['url']
    for member in message.new_chat_members:
        await bot.send_animation(chat_id=message.chat.id, animation=gif_data, caption=f'Добро пожаловать, {member.first_name}!')


# Удалить сообщение о том, что пользователь вышел
async def delete_goodbye_message(message: types.Message):
    try:
        await bot.delete_message(message.chat.id, message.message_id)
    except:
        print("Уже удалено")


# Регистрация хэндлеров
def register_handlers():
    dp.register_message_handler(echo_send)
    dp.register_message_handler(delete_channel_messages)
    dp.register_message_handler(welcome, content_types=types.ContentType.NEW_CHAT_MEMBERS)
    dp.register_message_handler(delete_goodbye_message, content_types=types.ContentType.LEFT_CHAT_MEMBER)


