n = int(input('Input natural number: '))

for num in range(1, n + 1):

    res = 1

    for i in range(1, num + 1):
        res *= 2

    if res > n:
        print(num - 1, int(res / 2))
        break