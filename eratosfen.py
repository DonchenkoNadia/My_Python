'''
все простые числа от 2 .. n

 2  3  4  5  6      9  n
[0, 0, 0, 0, 0, ... 0, 0]
[1, 1, 2, 1, 2, ... 2, 0]

Решето Эратосфена O(loglogN)
'''
n = 20
grid = [0]*n
grid[0], grid[1] = 0, 0
primes = []
lim = int(n**0.5)+1

def eratosthenes(n):     # n - число, до которого хотим найти простые числа
    sieve = list(range(n + 1))
    print(sieve)
    sieve[1] = 0    # без этой строки итоговый список будет содержать единицу
    print(sieve)
    for i in sieve:
        if i > 1:
            for j in range(i + i, len(sieve), i):
                sieve[j] = 0
    return sieve
print(eratosthenes(10))

'''
for j in range(2, lim):
    if grid[j] == 0:
        grid[j] == 1
        primes.append(j)
        k = 0
        while k + j < lim:
            k = k + j
            primes[k] = 2
            print(f"primes[{k}] = {primes[k]}")

    if primes[j] == 0:
        primes[j] = 1
        k = j
        while k < n:
            primes[k] = 2
            print(f"k = {k}")
            k *= j
    print(primes)
    '''
print(primes)
