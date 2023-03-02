# Установка Python в Docker
FROM python:latest
# Создание рабочей директории
WORKDIR /app
# Копирование туда файлов зависимости
COPY ./requirements.txt /app/requirements.txt
# Установка зависимостей
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
# Команда запуска кода
CMD [ "python", "main.py" ]
