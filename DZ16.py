import argparse

user = ["Max"]
password = ["indahouse"]


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
        help="Нужно ввести ваш логин, чтобы зайти в систему")

    parser.add_argument(
        "-d",
        "--password",
        type=str,
        help="Нужно ввести ваш пародь, чтобы зайти в систему")
    return parse


if __name__ == '__main__':
    a = 1
    while a <= 3:
        print('Введите логин:')
        l = parse().user = input()
        print('Введите пароль:')
        p = parse().pasword = input()
        if l not in user or p not in password or user.index(l) != password.index(p):
            if a <= 2:
                print('Неправильно. Попробуйте еще раз.')
            a += 1
        elif user.index(l) == password.index(p):
            print('Вы вошли.')
            break
        if a > 3:
            print('Вы исчерпали свои попытки.')