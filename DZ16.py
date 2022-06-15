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

    counter = 3
    while counter >= 1:

        print(f"У вас осталось {counter} попыток!")

        a = input("Логин: ")
        b = input("Пароль: ")

        if a == login and b != password:
            print("Неправильный Пароль!")
            counter -= 1
        elif a != login and b == password:
            print("Неправильный Логин!")
            counter -= 1
        elif a != login and b != password:
            print("Неправильный Логин и Пароль!!")
            counter -= 1
        else:
            print("Вы в системе =)")
            break
