numberList = [1, 9, 7, 4, 5, 20, 5, 6, 1]
index = 1  # счетчик прохода по списку, начнем со второго элемента (с индексом 1)
sosedi = 0  # счетчик "соседей"

# цикл прохода по списку, с1
while index < len(numberList) - 1:
    if numberList[index - 1] < numberList[index] > numberList[index + 1]:
        sosedi += 1
        index += 2
    else:
        index += 1
print(sosedi)