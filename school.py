from random import randint

n = 10
a = [0] * n
for i in range(n):
    a[i] = randint(10, 100)
for i in range(n):
    for j in range(i + 1, n):
        if a[i] % 10 > a[j] % 10:
            a[i], a[j] = a[j], a[i]
print(a)


n = 10
a = [0] * n
for i in range(n):
    a[i] = randint(0, 20)
a.sort()
print(*a)


n = 10
a = [0] * n
for i in range(n):
    a[i] = randint(10, 50)
find = int(input())
true = False
for i in range(n):
    if a[i] == find:
        print('A[', i, '] =', find)
        true = True
if not true:
    print('Не найден!')


input_ = int(input())
a = [input_]
while input_ != 0:
    a.append(input_)
    input_ = int(input())
while True:
    if min(a) % 3 == 0:
        print(min(a))
        break
    else:
        del a[min(a)]


n = 10
a = [0] * n
for i in range(n):
    a[i] = randint(0, 20)
a.sort(reverse=True)
print(a)


n = 20
a = [0] * n
for i in range(n):
    a[i] = randint(50, 150)
maximum = max(a)
minimum = min(a)
for i in range(n):
    if maximum == a[i]:
        print('Максимум: A[', i, '] =', maximum)
        break
for i in range(n):
    if minimum == a[i]:
        print('Минимум: A[', i, '] =', minimum)
        break
