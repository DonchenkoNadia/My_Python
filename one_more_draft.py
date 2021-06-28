n = 10
data = [-1]*n
data[0] = 0
data[1] = 1

def fib(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        if data[n-2] == -1:
            data[n-2] = fib(n-2)
        if data[n-1] == -1:
            data[n-1] = fib(n-1)
        else:
            return (data[n-2] + data[n-1])

print(fib(n))
