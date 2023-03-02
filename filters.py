from aiogram.dispatcher.filters import Filter
from aiogram import types


class IsChatAdmin(Filter):
    def __init__(self, permission: str):
        self.permission = permission

    async def check(self, message: types.Message):
        chat_member = await message.chat.get_member(message.from_user.id)
        return chat_member.is_chat_admin() and chat_member.can_restrict_members
