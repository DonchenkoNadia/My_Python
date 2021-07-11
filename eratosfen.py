'''
все простые числа от 2 .. n

 2  3  4  5  6      9  n
[0, 0, 0, 0, 0, ... 0, 0]
[1, 1, 2, 1, 2, ... 2, 0]

Решето Эратосфена O(loglogN)
'''
n = 10
primes = [0]*n
primes[2] = 1

for j in range(2, n):

    if primes[j] == 0:
        primes[j] = 1
        k = j
        while k < n:
            primes[k] = 2
            print(f"k = {k}")
            k *= j
    print(primes)
