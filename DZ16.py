import argparse
import datetime

logs = {"Max": "indahouse"}


def decorator(func):
    def wrapper(name: str, pwd: str) -> bool:
        if check_password(name, pwd):
            return func(name, pwd)
        else:
            return False

    return wrapper


class UserDoesNotExist(Exception):
    pass


@decorator
def login(name: str, pwd: str) -> bool:
    return True


def check_password(name: str, pwd: str) -> bool:
    if name in logs:
        raise UserDoesNotExist
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
            print("Неправильный Логин или Пароль!")
            counter -= 1
    else:
        print("Попыток больше нет.. Прощайте")

        deadline = datetime.datetime(2016, 2, 11, 15, 46, 20)
        print('Время последней попытки: {}.'.format(deadline.strftime('%d/%m/%Y %H:%M:%S')))
        now = datetime.datetime.now()
        if now >= deadline:
            print("Вы Заблокированы на 5 мин")