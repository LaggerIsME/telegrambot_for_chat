![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![image](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
![image](https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white)
![image](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![image](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
# Telegram-bot для Linux Klubа
Данный проект является нынешним чат-ботом Linux Klub-а, который выдает тэги пользователям, рассказывает анекдоты,
не разрешает выражаться нецензурной лексикой, а также может вести базовую беседу. Данные о возможных  плохих словах, о приветствиях и ссылки на гиф-изображения
хранятся внутри NoSQL MongoDB базы данных. Данные о спаме пользователя хранятся в NoSQL Redis базе данных. Бот общается по средством модели реализованной с помощью библиотеки scikit-learn.
Само общение бота с TelegramAPI реализовано с помощью Webhook-ов и Caddy веб-сервера
## Ссылка на бота: https://t.me/SulujhonBot
![image](other_documents/Ayano.jpg)
## Инструкция по использованию:
![image](other_documents/help.jpg)
## Функционал
* Общение с пользователями
* Выдавание и отбирание тэга у участников чата
* Выдача информации насчет клуба и правил его чата
* Фильтрация нецензурной речи
* Приветствие новых пользователей
* Удаление сообщений о уходе пользователей
* Рассказывание анекдотов про Linux
* Блокировка и запрет писать анонимно от лица каналов
* Блокировка ответа на сообщения, если пользователь начал спам
## Инструменты и библиотеки
* Aiogram
* Asyncio
* Caddy
* Scikit-learn
* PyMongo(MongoDB-Python)
* MongoDB
* Aioredis(Redis-Python)
* Redis
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
* Изменить значение переменных в файле `.env`
* Установить реверс-прокси Caddy с этого репозитория по инструкции: https://github.com/LaggerIsME/caddy_for_telegram_bot
* Запустить бота с помощью команды:
* * Linux: `docker compose up -d --build`
* * MacOS, Windows: `docker-compose up -d --build`

После всех этих действий бот будет доступен в Telegram по своему Telegram ID, приятного использования!
