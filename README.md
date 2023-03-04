![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![image](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
![image](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
# Telegram-bot для Linux Klubа
Данный проект является нынешним чат-ботом Linux Klub-а, который выдает тэги пользователям, рассказывает анекдоты,
не разрешает выражаться нецензурной лексикой, а также может вести базовую беседу. Данные о возможных  плохих словах, о приветствиях и ссылки на гиф-изображения
хранятся внутри NoSQL MongoDB базы данных. БД подключена через асинхронный драйвер AsyncIOMotor для высокой производительности.
## Ссылка на бота: https://t.me/SulujhonBot
<iframe src="https://assets.pinterest.com/ext/embed.html?id=42713896452182135" height="526" width="345" frameborder="0" scrolling="no" ></iframe>
## Функционал
* Ведение самого базового диалога
* Выдавание и отбирание тэга у участников чата
* Фильтрация нецензурной речи
* Приветствие новых пользователей
* Удаление сообщений о уходе пользователей
* Рассказывание анекдотов про Linux
* Блокировка и запрет писать анонимно от лица каналов
## Инструменты и библиотеки
* Aiogram
* Asyncio
* AsyncIOMotor(MongoDB-Python)
* MongoDB
* Docker
* Docker Compose
## Зависимости
* Python 3.10+
## Установка
* Клонировать репозиторий: `git clone https://github.com/LaggerIsME/telegrambot_for_chat`
* Скачать и установить Docker и Docker-Compose: https://docs.docker.com/engine/install/
* Перейти в директорию проекта: `cd ~/telegrambot_for_chat`
* Создать бота в Telegram и получить токен у @BotFather
* Также в чате с @BotFather написать: `/setprivacy` и поставить галочку на DISABLE
* Создать `token.json`, хранящий токен бота в виде: `{"token": "значение вашего токена"} `
* Запустить бота с помощью команды:
* * Linux: `docker compose up -d --build`
* * MacOS, Windows: `docker-compose up -d --build`

После всех этих действий бот будет доступен в Telegram по своему Telegram ID, приятного использования!