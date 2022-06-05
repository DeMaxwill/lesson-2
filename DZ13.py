def checkio(number: int) -> int:
    number = str(number)
    x = 1
    for i in number:
        if i == '0':
            x *= 1
        else:
            x *= int(i)

    return x


if __name__ == '__main__':
    print('Пример:')
    print(checkio(123405))

    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Готово? Поставь Лайк))")