from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/help')
b2 = KeyboardButton('/exe')
b3 = KeyboardButton('/donate')
b4 = KeyboardButton('/anecdote')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).add(b3).add(b4)