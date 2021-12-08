from collections import Counter
s = "anagram"
t = "mangaar"
count = Counter(s)
dict = {}
for ch in s:
    if ch not in dict:
        dict[ch] = 1
    else:
        dict[ch] += 1
print(count)
print(dict)

ans = 0
for ch in t:
    if dict[ch] > 0:
        dict[ch] -= 1
    else:
        ans += 1
print(ans)
