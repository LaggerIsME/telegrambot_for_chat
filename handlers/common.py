from aiogram import types
from main import generator
from bot_settings import dp, bot
from database import bad_words, gifs


# Проверка есть ли слово в предложении
async def findWord(string, word):
    return word.lower() in string.lower()


async def echo_simple_words_with_filter(message: types.Message, mode: bool):
    text = message.text.lower()
    text_split = text.split()
    # Если включили фильтр мата
    if mode:
        for i in text_split:
            if not i:
                await message.answer('Сообщение должно содержать хотя бы одно слово.')
                break
            elif bad_words.find_one({'bad_word': i}):
                await message.answer('Пожалуйста, не материтесь')
                # Удалить сообщение с матом
                await message.delete()
                break
    if not await findWord(message.text, 'сулу сулу'):
        # Сгенерировать ответ
        response = await generator.get_generative_replica(message.text)
        # Отправить его
        await message.answer(response)


async def echo_send(message: types.Message):
    # Если написали в ЛС
    if message.chat.type == types.ChatType.PRIVATE:
        await echo_simple_words_with_filter(message, mode=True)
    # Если в чат
    else:
        # Есть ли ответ на сообщение
        reply = message.reply_to_message
        # ID пользователя, которого отметили
        # Если отметили бота, то
        if reply:
            user = reply.from_user
            user_id = user.id
            if user_id == bot.id:
                # ID чата, в котором ответили боту
                await echo_simple_words_with_filter(message, mode=False)
        else:
            # Информация о боте
            bot_info = await bot.get_me()
            # Тэг бота
            bot_username = f"@{bot_info.username.lower()}"
            words = []
            # Разделить предложение на части по запятой
            for part in message.text.lower().split(","):
                # Разделить слова по пробелам
                words.extend(part.split())
            # Проверка слов
            for word in words:
                if word in ['сулу', 'сулужан', 'сулужанчик', bot_username]:
                    await echo_simple_words_with_filter(message, mode=False)
                    break


# Нужен чел с премиум, пока проверить нереально
# Удаляет сообщение и дает бан тем, кто пишет от канала
async def delete_channel_messages(message: types.Message):
    if message.chat.type == types.ChatType.CHANNEL:
        await message.delete()
        chat_id = message.chat.id
        await message.bot.restrict_chat_member(chat_id, message.from_user.id, can_send_messages=False)


# Приветствие для нового пользователя
async def welcome(message: types.Message):
    gif_doc = gifs.aggregate([{'$sample': {'size': 1}}]).next()
    gif_data = gif_doc['url']
    for member in message.new_chat_members:
        await bot.send_animation(chat_id=message.chat.id, animation=gif_data,
                                 caption=f'Добро пожаловать, {member.first_name}!\nПосмотреть правила чата: /rules')


# Удалить сообщение о том, что пользователь вышел
async def delete_goodbye_message(message: types.Message):
    try:
        await bot.delete_message(message.chat.id, message.message_id)
    except:
        pass


# Регистрация хэндлеров
def register_handlers():
    dp.register_message_handler(echo_send)
    dp.register_message_handler(delete_channel_messages)
    dp.register_message_handler(welcome, content_types=types.ContentType.NEW_CHAT_MEMBERS)
    dp.register_message_handler(delete_goodbye_message, content_types=types.ContentType.LEFT_CHAT_MEMBER)
