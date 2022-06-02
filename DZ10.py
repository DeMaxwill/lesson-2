a = {}
for w in input('Введите слова: ').split():
    a[w] = a.get(w, 0) + 1
    print(a[w] - 1, end=' ')