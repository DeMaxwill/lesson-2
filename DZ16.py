import argparse
import getpass

user = "Max"
password = "indahouse"


def decorator(func):
    def wrapper(name, pwd):
        if check_password(name, pwd):
            return func(name, pwd)
        else:
            return False

    return wrapper


@decorator
def check_login(name: str, pwd: str) -> bool:
    return password.get(name) == name


def check_password(name: str, pwd: str) -> bool:
    return password.get(pwd) == pwd


def parse():
    parser = argparse.ArgumentParser(description='Форма входа в систему')
    parser.add_argument(
        "-u",
        "--user",
        type=str,
        default=getpass.getuser(),
        help="Нужно ввести ваш логин, чтобы зайти в систему")

    parser.add_argument(
        "-d",
        "--password",
        type=str,
        help="Нужно ввести ваш пародь, чтобы зайти в систему")
    return parser.parse_args()


if __name__ == '__main__':

    if parse().user or input("Логин: ") and parse().password or input("Пароль: ") is True:
        print("Вы в системе =)")
    elif parse().user and parse().password is False:
        a = user or input("Логин: ")
        b = password or input("Пароль: ")
        c = counter = 3

        if a == user and b != password:
            print("Неправильный Пароль!")
            counter -= 1
        elif a != user and b == password:
            print("Неправильный Логин!")
            counter -= 1
        elif a != user and b != password:
            print("Неправильный Логин и Пароль!!")
            counter -= 1
        else:
            print("Вы в системе =)")
