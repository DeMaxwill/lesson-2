counter = 0
sum_attempts = 0
max_attempt = 0
min_attempt = 100
odd = 0
even = 0

while True:

    counter += 1

    ask = int(input('Ввести целое число: '))

    sum_attempts += ask


    if ask > max_attempt:
        max_attempt = ask


    if ask > min_attempt:
        min_attempt += ask


    if ask < min_attempt and ask != 0:
        min_attempt = ask


    if ask % 2 == 0 and ask != 0:
        even += 1


    if ask % 2 == 1:
        odd += 1

    if ask == 0:
        print("Attempts:", counter-1)
        print("Sum attempts:", sum_attempts)
        print("Arithmetic mean:", sum_attempts/(counter-1))
        print("Min int:", min_attempt)
        print("Max int:", max_attempt)
        print("Number of even int:", even)
        print("Number of odd int:", odd)
        break

