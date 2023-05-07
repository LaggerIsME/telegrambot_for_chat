# import types
# from aiogram.dispatcher.filters import Filter
#
# # Проверка, тот ли User
# class IsUser(Filter):
#     def __init__(self, uid):
#         self.uid = uid
#
#     async def check_user(self, message: types.Message):
#         user_id = message.from_user.id
#         if user_id == self.uid:
#             return True
#         else:
#             return False
#
# #
# #
# # class IsChatAdmin(Filter):
# #     def __init__(self, permission: str):
# #         self.permission = permission
# #
# #     async def check_admin(self, message: types.Message):
# #         chat_id = message.chat.id
# #         user_id = message.from_user.id
# #
# #         # Get information about the user's role in the chat
# #         chat_member = await message.chat.get_member(user_id)
# #
# #         # Check if the user is an administrator
# #         if chat_member.status in ('creator', 'administrator'):
# #             await message.answer('You are an admin in this chat!')
# #         else:
# #             await message.answer('You are not an admin in this chat.')
