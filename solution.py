def prefix(s):
    v = [0]*len(s)
    for i in range(1,len(s)):
        k = v[i-1]
        while k > 0 and s[k] != s[i]:
            k = v[k-1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return v

haystack = "a"
needle = ""
print(len(needle))

s1 = needle + "#" + haystack
pi = prefix(s1)
res = -1

for i in range(len(needle)+1, len(pi)):
    if pi[i] == len(needle):
        res = i-len(needle)*2
        break

print(res)
