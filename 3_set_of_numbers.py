from random import randint
N=int(input('количество элементов:'))
a = []
b = []
for i in range(0,N):
    a.append(randint(1,20))
    b.append(randint(1,20))

print ('массив a:', a)
print ('массив b:', b)

#входят одновременно в оба
two=set(a).intersection(set(b))
print('входят одновременно в оба массива:',sorted(two))

#входят только в первое, но не входят во второе
a1=[]
for i in range(0,N):
    if a[i] not in b:
        a1.append(a[i])
print('входят только в первый массив:', sorted(set(a1)))

#входят только во второе, но не входят в первое;
b1=[]
for i in range(0,N):
    if b[i] not in a:
        b1.append(b[i])
print('входят только во второй массив:', sorted(set(b1)))

#входят в первое или во второе, но не в оба из них одновременно.
c1=[]
for i in range(0,N):
    if a[i] not in two:
        c1.append(a[i])
    if b[i] not in two:
        c1.append(b[i])
print('входят в первый или во второй, но не в оба из них одновременно:', sorted(set(c1)))