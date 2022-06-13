logs = {"Max": "indahouse"}

def decorator (func):
    def wrapper(name, pwd):
        if check_password(name, pwd):
            return func(name, pwd)
        else:
            return False

    return wrapper

@decorator
def login(name: str, pwd: str) ->bool:
    return True


def check_password(name: str, pwd: str) -> bool:
    return logs.get(name)==pwd


if __name__ == '__main__':

    counter = 3
    while counter >= 1:

        print(f"У вас осталось {counter} попыток!")

        username = input("Логин: ")
        password = input("Пароль: ")

        log = login(username, password)

        if log is True:
            print("Вы в системе!")
            break
        else:
            print("Неправильный Логин или Пароль!")
            counter -= 1
    else:
        print("Попыток больше нет.. Прощайте")