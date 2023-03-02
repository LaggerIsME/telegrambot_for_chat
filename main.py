import json


# Получить токен бота
# path = путь к токену
def get_token(path: str = 'token.json'):
    try:
        # Открыть файл с токеном
        with open(path, 'r') as read_file:
            data = json.load(read_file)
        # Достать его из словаря
        token = data['token']
        return token
    except:
        print("Неправильно указан путь к файлу с токеном, либо сам файл неправильного формата")
        return False


def main():
    print(get_token())


if __name__ == '__main__':
    main()
