n = int(input())

h0, m0 = map(int, input().split())

while n != 0:
    h, m = map(int, input().split())
    if h == h0 and m == m0:
        c += 1
        if c > cash:
            cash = c
    else:
        c = 1
    h0 = h
    m0 = m
    n -= 1

print (cash)
