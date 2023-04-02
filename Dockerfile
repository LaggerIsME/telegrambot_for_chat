# Установка Python в Docker
FROM python:3.11.2
# Переход в рабочую директорию
WORKDIR /app
# Копирование туда файлов зависимости
COPY requirements.txt .
# Обновление инструментов
RUN pip install --upgrade setuptools
# Установка зависимостей
RUN pip install -r requirements.txt
# Скопировать все в наш образ
COPY . .

