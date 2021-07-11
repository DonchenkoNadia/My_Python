def countPrimes(n):
    if n == 2 or n == 0 or n == 1:
        return 0
    def isPrime(k):
        lim = int(k ** 0.5) + 1
        for i in range(2, lim):
            if k % i == 0:
                return 0
        return 1
    ans = 0
    for j in range(2, n):
        if isPrime(j):
            ans += 1
            print(j)
    return ans
print("Here we are")
print(countPrimes(3))
