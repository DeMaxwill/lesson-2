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
print("[papper] - Бумага ")
print("[lizard] - Ящерица")
print("[spock] - Спок")

player_score = 0
player_select = 0
comp_score = 0
comp_select = 0

print("-----------------------------------------------------")
print("------------------Игра Началась----------------------")

while True:
    for i in range(3):
        print("-------РАУНД №" + str(i + 1) + "--")
        rpsls = "rock", "scissors", "papper", "lizard", "spock"
        comp_select = random.choice(rpsls)
        while True:
            player_select = input("Сделайте ваш выбор: ")
            print("Игрок: " + player_select)
            if (player_select == "rock") or (player_select == "scissors") or (player_select == "papper") \
                    or (player_select == "lizard") or (player_select == "spock"):
                break
            else:
                print(f"Invalid input " + '"' + player_select + '"')
        print("Компьютер: " + comp_select)
        if player_select == comp_select:
            print("<<Ничья>>")
        elif player_select == "rock" and comp_select == "scissors":
            player_score = player_score + 1
            print("$$$ Вы Выиграли $$$")
        elif player_select == "rock" and comp_select == "lizard":
            player_score = player_score + 1
            print("$$$ Вы Выиграли $$$")
        elif player_select == "rock" and comp_select == "papper":
            comp_score = comp_score + 1
            print("ХХХ Выиграл Компьютер ХХХ")
        elif player_select == "rock" and comp_select == "spock":
            comp_score = comp_score + 1
            print("ХХХ Выиграл Компьютер ХХХ")
        elif player_select == "rock" and comp_select == "papper":
            comp_score = comp_score + 1
            print("ХХХ Выиграл Компьютер ХХХ")
        elif player_select == "papper" and comp_select == "rock":
            player_score = player_score + 1
            print("$$$ Вы Выиграли $$$")
        elif player_select == "papper" and comp_select == "spock":
            player_score = player_score + 1
            print("$$$ Вы Выиграли $$$")
        elif player_select == "papper" and comp_select == "scissors":
            comp_score = comp_score + 1
            print("ХХХ Выиграл Компьютер ХХХ")
        elif player_select == "papper" and comp_select == "lizard":
            comp_score = comp_score + 1
            print("ХХХ Выиграл Компьютер ХХХ")
        elif player_select == "scissors" and comp_select == "papper":
            player_score = player_score + 1
            print("$$$ Вы Выиграли $$$")
        elif player_select == "scissors" and comp_select == "lizard":
            player_score = player_score + 1
            print("$$$ Вы Выиграли $$$")
        elif player_select == "scissors" and comp_select == "rock":
            comp_score = comp_score + 1
            print("ХХХ Выиграл Компьютер ХХХ")
        elif player_select == "scissors" and comp_select == "spock":
            comp_score = comp_score + 1
            print("ХХХ Выиграл Компьютер ХХХ")
        elif player_select == "lizard" and comp_select == "papper":
            player_score = player_score + 1
            print("$$$ Вы Выиграли $$$")
        elif player_select == "lizard" and comp_select == "spock":
            player_score = player_score + 1
            print("$$$ Вы Выиграли $$$")
        elif player_select == "lizard" and comp_select == "rock":
            comp_score = comp_score + 1
            print("ХХХ Выиграл Компьютер ХХХ")
        elif player_select == "lizard" and comp_select == "scissors":
            comp_score = comp_score + 1
            print("ХХХ Выиграл Компьютер ХХХ")
        elif player_select == "spock" and comp_select == "rock":
            player_score = player_score + 1
            print("$$$ Вы Выиграли $$$")
        elif player_select == "spock" and comp_select == "scissors":
            player_score = player_score + 1
            print("$$$ Вы Выиграли $$$")
        elif player_select == "spock" and comp_select == "papper":
            comp_score = comp_score + 1
            print("ХХХ Выиграл Компьютер ХХХ")
        elif player_select == "spock" and comp_select == "lizard":
            comp_score = comp_score + 1
            print("ХХХ Выиграл Компьютер ХХХ")
    print("------------------------------------")
    print("----------Финальные Очки------------")
    if player_score > comp_score:
        print("***Поздравляем! Вы Победитель!***")
        print(f"Компьютер - {comp_score}, Игрок - {player_score}")
        print("-------------------------------------------------")
        print("Играем еще раз? Да или Нет")
        reset = input()
    elif player_score < comp_score:
        print("***Вы Проиграли =( Компьютер Победил!***")
        print(f"Компьютер - {comp_score}, Игрок - {player_score}")
        print("-------------------------------------------------")
        print("Играем еще раз? Да или Нет")
        reset = input()
    else:
        print("!!!Ничья!!!")
        print(f"Компьютер - {comp_score}, Игрок - {player_score}")
        print("-------------------------------------------------")
        print("Играем еще раз? Да или Нет")
        reset = input()
    if reset == "Да":
        continue
    elif reset == "Нет":
        break
    else:
        print(f"Invalid input " + '"' + reset + '"')
