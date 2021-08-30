s = "a a bb     aa"
l = 0
r = len(s)-1

while l < r:
    if s[l] == " ":
        l += 1
    if s[r] == " ":
        r -= 1
    if s[l] == s[r]:
        l += 1
        r -= 1
    else:
        print("string is not polindrom ")
        break
print("string is perfect polindrom")
