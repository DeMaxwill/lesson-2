n = int(input('Начало: '))
min = max = n
while n != 0:
   if n > max:
     max = n
   if n < min:
     min = n
   n = int(input('Завершение: '))
print(f'max = {max}\nmin = {min}')
