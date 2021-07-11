a = 2
b = 100
diff = 4
first_prime = -1
second_prime = -1
primes = []

def isPrime(n):
    m = int(n**0.5) + 1
    for i in range (2, m + 1):
        if n % i == 0:
            return 0
    return 1

for j in range(a, b+1):
    if isPrime(j):
        primes.append(j)

print(primes)
l = 0
r = 1
while r < len(primes):
    if primes[r] - primes[l] == diff:
        print(f"Answer found! - {primes[l]} and {primes[r]}")
    if primes[r] - primes[l] < diff:
        r += 1
# зафиксировать левую границу и предвигать правую в поиске значение primes[l] + diff
# если такого значения не нашли, то передвинуть левый указатель. и так до конца списка
        




        #if primes[1] - primes[0] == diff:
            #print(f"Answer found! - {primes}")
