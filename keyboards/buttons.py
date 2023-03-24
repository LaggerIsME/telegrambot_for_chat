from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from bot_settings import bot

b1 = KeyboardButton('/start')
b2 = KeyboardButton('/help')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2)


# Установить подсказки для комманд
async def set_commands():
    bot_commands = [
        types.BotCommand(command="/start", description="Начать диалог со мной"),
        types.BotCommand(command="/help", description="Инструкция по использованию"),
        types.BotCommand(command="/donate", description="Реквизиты для донатов в хостинг бота"),
        types.BotCommand(command="/faq", description="Ответы на часто задаваемые вопросы Linux Klub-у"),
        types.BotCommand(command="/about", description="Информация о самом Linux Klub"),
        types.BotCommand(command="/rules", description="Правила чата Linux Klub"),
        types.BotCommand(command="/exe", description="Исходники данного бота"),
        types.BotCommand(command="/anecdote", description="Рандомный анекдот на тему Linux"),
        types.BotCommand(command="/set_nickname", description="Выдача тэга пользователю внутри чата\n(Доступ только у "
                                                              "администраторов с правом выбора других "
                                                              "администраторов)"),
        types.BotCommand(command="/clear_nickname", description="Отбирание тэга у пользователя внутри чата\n(Доступ "
                                                                "только у владельца чата)"),
        types.BotCommand(command="/top100", description="Топ 100 человек, поддержавших данный проект"),
    ]
    await bot.set_my_commands(bot_commands)