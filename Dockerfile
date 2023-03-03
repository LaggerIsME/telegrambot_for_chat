# Установка Python в Docker
FROM python:latest
# Переход в рабочую директорию
WORKDIR /app
# Копирование туда файлов зависимости
COPY requirements.txt .
# Установка зависимостей
RUN pip install -r --upgrade requirements.txt
# Скопировать остальное
COPY . .
# Переход в директорию с модулем базы данных
WORKDIR /app/database
# Активация скрипта для заполнения MongoDB NoSQL
RUN python import_data_in_db.py
# Переход в директорию приложения
WORKDIR /app
# Запуск приложения
CMD ["python", "main.py"]