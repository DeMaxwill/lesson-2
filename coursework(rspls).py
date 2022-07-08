import random

print("----------------------------------------------------")
print("-------Камень, Ножницы, Бумага, Ящерица, Спок-------")
print("------------!Добро пожаловать в Игру!---------------")
print("----------------Игра в три раунда.------------------")
print("-------------------Правила--------------------------")
f = open("rules.txt")
data = f.read()
print(data)
f.close()
print("[rock] - Камень ")
print("[scissors] - Ножницы ")
print("[paper] - Бумага ")
print("[lizard] - Ящерица")
print("[spock] - Спок")

count = [0, 0]

print("-----------------------------------------------------")
print("------------------Игра Началась----------------------")


def main():
    while True:
        for i in range(3):
            print("-------РАУНД №" + str(i + 1) + "--")
            rpsls = "rock", "scissors", "paper", "lizard", "spock"
            comp_select = random.choice(rpsls)
            while True:
                player_select = input("Ваш выбор?\n>>> ").lower()

                if (player_select == "rock") or (player_select == "scissors") or (player_select == "paper") \
                        or (player_select == "lizard") or (player_select == "spock"):
                    break
                else:
                    print(f"Invalid input " + '"' + player_select + '"')
            print("Игрок: " + player_select)
            print("Компьютер: " + comp_select)
            if player_select == comp_select:
                print("<<Ничья>>")
            elif player_select == "rock" and comp_select == "scissors":
                print("$$$ Вы Выиграли $$$")
                count[0] += 1
            elif player_select == "rock" and comp_select == "lizard":
                print("$$$ Вы Выиграли $$$")
                count[0] += 1
            elif player_select == "rock" and comp_select == "paper":
                print("ХХХ Выиграл Компьютер ХХХ")
                count[1] += 1
            elif player_select == "rock" and comp_select == "spock":
                print("ХХХ Выиграл Компьютер ХХХ")
                count[1] += 1
            elif player_select == "rock" and comp_select == "paper":
                print("ХХХ Выиграл Компьютер ХХХ")
                count[1] += 1
            elif player_select == "paper" and comp_select == "rock":
                print("$$$ Вы Выиграли $$$")
                count[0] += 1
            elif player_select == "paper" and comp_select == "spock":
                print("$$$ Вы Выиграли $$$")
                count[0] += 1
            elif player_select == "paper" and comp_select == "scissors":
                print("ХХХ Выиграл Компьютер ХХХ")
                count[1] += 1
            elif player_select == "paper" and comp_select == "lizard":
                print("ХХХ Выиграл Компьютер ХХХ")
                count[1] += 1
            elif player_select == "scissors" and comp_select == "paper":
                print("$$$ Вы Выиграли $$$")
                count[0] += 1
            elif player_select == "scissors" and comp_select == "lizard":
                print("$$$ Вы Выиграли $$$")
                count[0] += 1
            elif player_select == "scissors" and comp_select == "rock":
                print("ХХХ Выиграл Компьютер ХХХ")
                count[1] += 1
            elif player_select == "scissors" and comp_select == "spock":
                print("ХХХ Выиграл Компьютер ХХХ")
                count[1] += 1
            elif player_select == "lizard" and comp_select == "paper":
                print("$$$ Вы Выиграли $$$")
                count[0] += 1
            elif player_select == "lizard" and comp_select == "spock":
                print("$$$ Вы Выиграли $$$")
                count[0] += 1
            elif player_select == "lizard" and comp_select == "rock":
                print("ХХХ Выиграл Компьютер ХХХ")
                count[1] += 1
            elif player_select == "lizard" and comp_select == "scissors":
                print("ХХХ Выиграл Компьютер ХХХ")
                count[1] += 1
            elif player_select == "spock" and comp_select == "rock":
                print("$$$ Вы Выиграли $$$")
                count[0] += 1
            elif player_select == "spock" and comp_select == "scissors":
                print("$$$ Вы Выиграли $$$")
                count[0] += 1
            elif player_select == "spock" and comp_select == "paper":
                print("ХХХ Выиграл Компьютер ХХХ")
                count[1] += 1
            elif player_select == "spock" and comp_select == "lizard":
                print("ХХХ Выиграл Компьютер ХХХ")
                count[1] += 1
        print("------------------------------------")
        print("----------Финальные Очки------------")
        if count[0] > count[1]:
            print("***Поздравляем! Вы Победитель!***")
            print(f"Игрок - {count[0]}, Компьютер - {count[1]}")
            print("------------------------------------")
            ask_user()
        elif count[0] < count[1]:
            print("***Вы Проиграли =( Компьютер Победил!***")
            print(f"Игрок - {count[0]}, Компьютер - {count[1]}")
            print("------------------------------------")
            ask_user()
        else:
            print("!!!Ничья!!!")
            print(f"Игрок - {count[0]}, Компьютер - {count[1]}")
            print("------------------------------------")
            ask_user()


def ask_user():
    check = str(input("Играем еще раз? да или нет\n>>> ")).lower().strip()
    try:
        if check == 'да':
            return main()
        elif check == 'нет':
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
