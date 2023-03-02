import types
from aiogram.dispatcher.filters import Command
from filters import IsChatAdmin
from bot_settings import dp

async def command_give_nickname(message: types.Message):


# Регистрация хэндлеров
def register_handlers():
    dp.register_message_handler(command_give_nickname, Command('help'), IsChatAdmin('can_restrict_members'))
