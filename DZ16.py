import json
import argparse
import datetime


def decorator(func):
    def wrapper(name: str, pwd: str) -> bool:
        try:
            if not check_password(name, pwd):
                print("Неверный Пароль!")
                return False
            else:
                return func(name, pwd)
        except UserDoesNotExist as a:
            print(a)
            return False

    return wrapper


class UserDoesNotExist(Exception):
    pass


@decorator
def login(name: str, pwd: str) -> bool:
    return True


def check_password(name: str, pwd: str) -> bool:
    with open('reg.json', 'r') as f:
        logs = json.loads(f.read())
        if name not in logs:
            raise UserDoesNotExist("Неверный Логин!")
        else:
            return logs.get(name) == pwd


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', type=str, help='username')
    parser.add_argument('-p', '--password', type=str, help='password')
    return parser.parse_args()


if __name__ == '__main__':

    counter = 3
    while counter >= 1:

        print(f"У вас осталось {counter} попыток!")

        username = parse().user or input("Логин: ")
        password = parse().password or input("Пароль: ")

        if login(username, password):
            print("Вы в системе!")
            break
        else:
            counter -= 1
    else:
        print("Попыток больше нет..")

        deadline = datetime.datetime(2016, 2, 11, 15, 46, 20)
        print('Время последней попытки: {}.'.format(deadline.strftime('%d/%m/%Y %H:%M:%S')))
        now = datetime.datetime.now()
        if now >= deadline:
            print("Вы Заблокированы на 5 мин")
