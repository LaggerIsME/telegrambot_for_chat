from aiogram import types
from bot_settings import dp, bot
from keyboards import kb_client
from database import anecdotes, instructions


async def get_instructions(_id: str):
    instruction = await instructions.find_one({'_id': _id}, {'id': 0})
    instruction = instruction['text']
    return instruction
# @dp.message_handler(commands=['start'])


async def command_start(message: types.Message):
    try:
        if message.chat.type == types.ChatType.PRIVATE:
            await message.answer('Привет, меня зовут Сулужан, чтоб узнать о моих функциях напишите /help',
                                 reply_markup=kb_client)
        else:
            await message.answer('Привет, меня зовут Сулужан, чтоб узнать о моих функциях напишите /help')
    # Если не может писать
    except:
        await message.answer('У меня какие-то проблемы, простите')


async def command_exe(message: types.Message):
    try:
        if message.chat.type == types.ChatType.PRIVATE:
            await message.answer('Мои исходники:https://github.com/LaggerIsME/telegrambot_for_chat',
                                 reply_markup=kb_client)
        else:
            await message.answer('Мои исходники:https://github.com/LaggerIsME/telegrambot_for_chat')
    # Если не может писать
    except:
        await message.answer('У меня какие-то проблемы, простите')


# @dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    try:
        photo = open('other_documents/help.jpg', 'rb')
        await bot.send_photo(chat_id=message.chat.id, photo=photo)
    # Если не может писать
    except:
        await message.answer('У меня какие-то проблемы, простите')


async def command_faq(message: types.Message):
    faq = await get_instructions('faq')
    try:
        await message.answer(faq)
    # Если не может писать
    except:
        await message.answer('У меня какие-то проблемы, простите')


async def command_donate(message: types.Message):
    donate = await get_instructions('donate')
    try:
        await message.answer(donate)
    # Если не может писать
    except:
        await message.answer('У меня какие-то проблемы, простите')


async def command_about(message: types.Message):
    about = await get_instructions('about')
    try:
        await message.answer(about)
    # Если не может писать
    except:
        await message.answer('У меня какие-то проблемы, простите')


async def command_rules(message: types.Message):
    rules = await get_instructions('rules')
    try:
        await message.answer(rules)
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


# Поставить никнейм
async def command_set_nickname(message: types.Message):
    # Проверка пишет ли пользователь в ЛС
    if message.chat.type != types.ChatType.PRIVATE:
        # Проверка отметите ли кого-либо
        reply = message.reply_to_message
        if not reply:
            return
        user = reply.from_user
        if not user:
            return
        # ID чата, в котором запросили смену тэг
        chat_id = message.chat.id
        # ID пользователя, которому нужно сменить тэг
        user_id = user.id
        command_user_id = message.from_user.id
        # Получение информацию о пользователе
        chat_member = await message.chat.get_member(user_id)
        command_user = await message.chat.get_member(command_user_id)
        # Если пользователь не бот
        if user_id != bot.id:
            # Если пользователь админ или создатель,то
            if (command_user.is_chat_admin() or command_user.is_chat_owner()) \
                    and not chat_member.is_chat_owner():
                # Если есть значение никнейма
                bot_info = await bot.get_me()
                bot_username = f"@{bot_info.username}"
                # Вырезать /set_nickname
                args = message.text.replace("/set_nickname", "").strip()
                # Вырезать имя бота из ника
                args = args.replace(bot_username, "").strip()
                if len(args) >= 1:
                    if user_id == command_user_id or command_user.can_promote_members:
                        # Повышение прав до админа, который может приглашать пользователей
                        await message.bot.promote_chat_member(chat_id, user_id, can_invite_users=True)
                        # Смена тэга пользователя
                        await message.bot.set_chat_administrator_custom_title(chat_id, user_id, args)
                        await message.answer(f"Пользователю {user.full_name} был установлен тэг {args}")
                    else:
                        await message.answer('У вас недостаточно прав')
                else:
                    await message.answer('Введите значение после команды /set_nickname')
            else:
                await message.answer('У вас недостаточно прав')
        else:
            await message.answer("Я не могу сама себе поставить никнейм")
    else:
        await message.answer('Это функция лишь для чата, я не могу поставить тэг в чате с пользователем')


async def command_clear_nickname(message: types.Message):
    # Проверка пишет ли пользователь в ЛС
    if message.chat.type != types.ChatType.PRIVATE:
        # Проверка отметите ли кого-либо
        reply = message.reply_to_message
        if not reply:
            return
        user = reply.from_user
        if not user:
            return
        # ID чата, в котором запросили смену тэг
        chat_id = message.chat.id
        # ID пользователя, которому нужно сменить тэг
        command_user_id = message.from_user.id
        user_id = user.id
        # Получение информацию о пользователе
        chat_member = await message.chat.get_member(user_id)
        command_user = await message.chat.get_member(command_user_id)
        # Если пользователь создатель, то
        if command_user.is_chat_owner() and not chat_member.is_chat_owner():
            await message.bot.promote_chat_member(chat_id, user_id, is_anonymous=False, can_manage_chat=False,
                                                  can_post_messages=False, can_edit_messages=False,
                                                  can_delete_messages=False, can_manage_video_chats=False,
                                                  can_restrict_members=False, can_promote_members=False,
                                                  can_change_info=False, can_invite_users=False, can_pin_messages=False,
                                                  can_manage_topics=False, )
            await message.answer(f"У пользователя {user.full_name} был забран тэг")
        else:
            await message.answer('У вас недостаточно прав')

    else:
        await message.answer('Это функция лишь для чата, я не могу убрать тэг в чате с пользователем')


# Регистрация хэндлеров
def register_handlers():
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(command_faq, commands=['faq'])
    dp.register_message_handler(command_donate, commands=['donate'])
    dp.register_message_handler(command_about, commands=['about'])
    dp.register_message_handler(command_rules, commands=['rules'])
    dp.register_message_handler(command_exe, commands=['exe'])
    dp.register_message_handler(command_anecdote, commands=['anecdote'])
    dp.register_message_handler(command_set_nickname, commands=['set_nickname'])
    dp.register_message_handler(command_clear_nickname, commands=['clear_nickname'])
