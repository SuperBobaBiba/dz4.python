from random import randint
N=int(input('количество элементов:'))
a = []
for i in range(0,N):
    a.append(randint(1,100))

print ('сгенерированный массив:', a)



for i in range(N - 1):
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print ('Отсортированный массив:', a)


