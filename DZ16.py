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
def login(name: str, pwd: str) -> bool:
    return True


def check_password(name: str, pwd: str) -> bool:
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

        log = login(username, password)
        pas = check_password(username, password)

        if log and pas is True:
            print("Вы в системе!")
            break
        else:
            print("Неправильный Логин или Пароль!")
            counter -= 1
    else:
        print("Попыток больше нет.. Прощайте")

