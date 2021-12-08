def check(a):
    print(№a)

def find(i):
    if i == k:
        check(a)
        return
    a[i] = 0
    find(i + 1)
    a[i] = 1
    find(i + 1)

k = 3
a = [None] * k
find(0)
