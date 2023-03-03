from aiogram import types
from bot_settings import dp
from keyboards import kb_client
from database import anecdotes


# @dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    try:
        if message.chat.type == types.ChatType.PRIVATE:
            await message.answer('Привет, меня зовут Сулужан, чтоб узнать о моих функциях напишите /help', reply_markup=kb_client)
        else:
            await message.answer('Привет, меня зовут Сулужан, чтоб узнать о моих функциях напишите /help')
    # Если не может писать
    except:
        await message.answer('У меня какие-то проблемы, простите')


# @dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    try:
        if message.chat.type == types.ChatType.PRIVATE:
            await message.answer('Мои команды:\n/start - начать	диалог со мной\n/help -	инструкция по '
                                 'использованию\n/anecdote - выдает рандомный анекдот на	тему Linux\n/set_nickname - '
                                 'выдает тэг пользователю внутри чата\n(Доступ только у '
                                 'администраторов)\n/clear_nickname	- забирает тэг пользователя внутри чата\n(Доступ	'
                                 'только у владельца чата)\n\nМои функции:\n* Ведение самого базового диалога\n* '
                                 'Выдавание и отбирание тэга у участников чата\n* Фильтрация нецензурной речи\n* '
                                 'Приветствие новых пользователей\n* Удаление сообщений о уходе пользователей\n* '
                                 'Рассказывание анекдотов про Linux\n* Блокировка и запрет писать анонимно от лица '
                                 'каналов\n\nМои исходники:https://github.com/LaggerIsME/telegrambot_for_chat',
                                 reply_markup=kb_client)
        else:
            await message.answer('Мои команды:\n/start - начать	диалог со мной\n/help -	инструкция по '
                                 'использованию\n/anecdote - выдает рандомный анекдот на	тему Linux\n/set_nickname - '
                                 'выдает тэг пользователю внутри чата\n(Доступ только у '
                                 'администраторов)\n/clear_nickname	- забирает тэг пользователя внутри чата\n(Доступ	'
                                 'только у владельца чата)\n\nМои функции:\n* Ведение самого базового диалога\n* '
                                 'Выдавание и отбирание тэга у участников чата\n* Фильтрация нецензурной речи\n* '
                                 'Приветствие новых пользователей\n* Удаление сообщений о уходе пользователей\n* '
                                 'Рассказывание анекдотов про Linux\n* Блокировка и запрет писать анонимно от лица '
                                 'каналов\n\nМои исходники:https://github.com/LaggerIsME/telegrambot_for_chat',
                                 )
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
        # Получение информацию о пользователе
        chat_member = await message.chat.get_member(user_id)
        command_user = await message.chat.get_member(message.from_user.id)
        # Если пользователь админ или создатель,то
        if (command_user.is_chat_admin() or command_user.is_chat_owner()) and not chat_member.is_chat_owner():
            # Если есть значение никнейма
            args = message.text.split()
            if len(args) >= 2:
                # Значение никнейма после пробела
                arg = args[1]
                # Повышение прав до админа, который может приглашать пользователей
                await message.bot.promote_chat_member(chat_id, user_id, can_invite_users=True)
                # Смена тэга пользователя
                await message.bot.set_chat_administrator_custom_title(chat_id, user_id, arg)
                await message.answer(f"Пользователю {user.full_name} был установлен тэг {arg}")
            else:
                await message.answer('Введите значение после команды /set_nickname')
        else:
            await message.answer('У вас недостаточно прав')
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
        user_id = user.id
        # Получение информацию о пользователе
        chat_member = await message.chat.get_member(user_id)
        command_user = await message.chat.get_member(message.from_user.id)
        # Если пользователь создатель, то
        if command_user.is_chat_owner() and not chat_member.is_chat_owner():
            await message.bot.promote_chat_member(chat_id, user_id, is_anonymous=False, can_manage_chat=False,
                                                      can_post_messages=False, can_edit_messages=False,
                                                      can_delete_messages=False, can_manage_video_chats=False,
                                                      can_restrict_members=False, can_promote_members=False,
                                                      can_change_info=False, can_invite_users=False, can_pin_messages=False,
                                                      can_manage_topics=False,)
            await message.answer(f"У пользователя {user.full_name} был забран тэг")
        else:
            await message.answer('У вас недостаточно прав')

    else:
        await message.answer('Это функция лишь для чата, я не могу убрать тэг в чате с пользователем')


# Регистрация хэндлеров
def register_handlers():
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(command_anecdote, commands=['anecdote'])
    dp.register_message_handler(command_set_nickname, commands=['set_nickname'])
    dp.register_message_handler(command_clear_nickname, commands=['clear_nickname'])


