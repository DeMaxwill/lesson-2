import argparse
import getpass

login = "Max"
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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Форма входа в систему')
    parser.add_argument(
        "-u",
        "--user",
        default=getpass.getuser(),
        help="Нужно ввести ваш логин, чтобы зайти в систему")

    parser.add_argument(
        "-d",
        "--password",
        help="Нужно ввести ваш пародь, чтобы зайти в систему")

    options = parser.parse_args()
    if options.password and options.user is True:
        user = options.user
        password = options.password
        auth = {user: password}
    else:

        c = 3
    while c >= 1:

        print(f"У вас осталось {c} попыток!")

        a = login
        b = password

        if a == login and b != password:
            print("Неправильный Пароль!")
            c -= 1
        elif a != login and b == password:
            print("Неправильный Логин!")
            c -= 1
        elif a != login and b != password:
            print("Неправильный Логин и Пароль!!")
            c -= 1
        else:
            print("Вы в системе =)")
            break
