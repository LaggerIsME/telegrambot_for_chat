from aiogram import types
from aiogram.dispatcher.filters import Command
from filters import IsChatAdmin
from bot_settings import dp


async def command_set_nickname(message: types.Message):
    reply = message.reply_to_message
    print(reply)
    if not reply:
        return
    user = reply.from_user
    if not user:
        return
    chat_id = message.chat.id
    user_id = user.id
    args = message.text.split()[1]
    can_invite_users = True
    await message.bot.promote_chat_member(chat_id, user_id, can_invite_users)
    if args:
        await message.bot.set_chat_administrator_custom_title(chat_id, user_id, args)
    await message.answer(f"User {user.full_name} promoted to admin")


# Регистрация хэндлеров
def register_handlers():
    dp.register_message_handler(command_set_nickname, Command('set_nickname'), IsChatAdmin('can_restrict_members'))
