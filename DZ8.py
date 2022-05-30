a = list(input().split())
a = [int(i) for i in a]
a.sort()
a.reverse()
x = int(input())
for i in range(len(a)):
    if a[i] < x:
        print(i + 1)
        exit()
print(len(a) + 1)