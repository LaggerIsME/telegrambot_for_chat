# Установка Python в Docker
FROM python:latest
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

