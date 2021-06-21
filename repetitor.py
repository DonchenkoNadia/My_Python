a = int(input())
b = int(input())

YES, if true

a = {xyxyyx}
b = {xyyxyx}

len_a = a.bit_length()
len_b = b.bit_length()
i = 0

if len_a != len_b:
    print ("NO")
    break

for i in range(0, len_a // 2 + 1):

    if getbit(a, len_a - i - 1) != getbit(b, i):
        print("NO")
        break


getbit(a, len_a - 1) --- getbit(b, 1)
a[len_a - 1] -- b[1]

.....


L    2 0
10101001

  L    0
  101010
  xxxxx1
  ------
  000000


getbit(a, 2) -> 1


n
n чисел

все числа парные, кроме одного
вывести это число



5
[7 1 1 4 7]

res = 0
res = res xor a[0] // 7

res = res xor a[1] // 6
111
001
110 == 6

res = res xor a[2] // 7
110
001
111 == 7

res = res xor a[3] // 3
111
100
011

res = res xor a[4] // 4
011
111
100

4

xor

7 xor 5 == 2

111 == 7
101 == 5
---
010 == 2

c = a xor b


2 непарных
делаем точно так же?
тогда по результату мы будем иметь p1 xor p2


1) попробовать доделать 2 указателя; если не ОК до вск (до утра) - пиши мне, обсудим
1.1) запустить прошлый код из атома
2) реализовать нахождение 1го непарного
2+) leetcode взять задачи на битовые операции и порешать их
