def login():
  for t in reversed(range(4)):
    ll= input("Введите логин: ")
    p = input('Введите пароль: ')
    if p == 'indahouse':
       if ll == 'Max':
        print('Вы в системе!')
        break
    if t > 0:
        print('Осталось попыток', t)
  else:
    print('Не правильное Имя или Пароль')
login()