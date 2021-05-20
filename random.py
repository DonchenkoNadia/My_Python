a = "1010"
b = "1011"
n = max(len(a), len(b))
a, b = a.zfill(n), b.zfill(n)
res = []
carry = 0

for i in range(n-1, -1, -1):

    if a[i] == "1":
        carry += 1
    if b[i] == "1":
        carry += 1
    if carry % 2 == 1:
        res.append("1")
    if carry % 2 == 0:
        res.append("0")

    carry //= 2

if carry == 1:
    res.append("1")
res.reverse()

print("".join(res))
