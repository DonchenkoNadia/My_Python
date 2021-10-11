ans = i = 0
s = "XXOX"

while i < len(s):
    if s[i] == "X":
        ans += 1
        i += 3
    else:
        i += 1

print(ans)
