import argparse

logs = {"Max": "indahouse"}


def decorator(func):
    def wrapper(name, pwd):
        if check_password(name, pwd):
            return func(name, pwd)
        else:
            return False

    return wrapper


@decorator
def login(name: str, pwd: str,) -> bool:
    return logs.get(pwd) == name


def check_password(name: str, pwd: str) -> bool:
    return logs.get(name) == pwd


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--user', type=str, help='username')
    parser.add_argument('-p', '--password', type=str, help='password')
    return parser.parse_args()


if __name__ == '__main__':

    for i in range(3):
        name = parse().user or input("Логин: ")
        password = parse().password or input('Пароль: ')
        num_name = 0
        num_pwd = 0
        login(name, password)
        check_password(name, password)

        if name == 'Max':
            num_name = 1
        else:
            num = name = 0
        if password == 'indahouse':
            num_pwd = 1
        else:
            num_pwd = 0
        sum = num_name + num_pwd
        if sum == 2:
            print('Вошли успешно! ')
            break
        elif i == 2 and sum != 2:
            print('3 раза неверно имя пользователя или пароль! Выход из системы!')
            break
        else:
            continue
