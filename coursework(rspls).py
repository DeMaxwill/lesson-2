from random import choice

print("-------Камень, Ножницы, Бумага, Ящерица, Спок-------")
print("------------!Добро пожаловать в Игру!---------------")
print("-------------------Правила--------------------------")
f = open("rules.txt")
data = f.read()
print(data)
f.close()


rspls = {"камень": ["ножницы", "ящерица"],
         "ножницы": ["бумага", "ящерица"],
         "бумага": ["камень", "спок"],
         "спок": ["ножницы", "камень"],
         "ящерица": ["бумага", "спок"]}


def main():

    player_select = input("Ваш Выбор (камень, ножницы, бумага, ящерица или спок)?\n>>> ").lower()

    if player_select not in rspls:
        print(f"Invalid input " + '"' + player_select + '"')
        main()
    else:
        comp_select = choice("камень/ножницы/бумага/ящерица/спок".split("/"))

        print("Игрок: " + player_select)
        print("Компьютер: " + comp_select)

        if player_select == comp_select:
            print('Ничья!')
            ask_user()
        else:
            if player_select in rspls[comp_select]:
                print('Компьютер Выйграл!')
                ask_user()
            else:
                print('Игрок Выйграл!')
                ask_user()


def ask_user():
    check = str(input("Продолжить? y/n\n>>> ")).lower().strip()
    try:
        if check == 'y':
            return main()
        elif check == 'n':
            exit()
        else:
            print(f"Invalid input " + '"' + check + '"')
            return ask_user()
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        return ask_user()


if __name__ == "__main__":
    main()
    ask_user()
