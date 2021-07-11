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

s = 'abac'
print(prefix(s))

n = len(s)
pi = prefix(s)
k = n - pi[n-1]
print(k)
print(n % k)

if n % k == 0 and k > 0:
    print(s[0:k])
else:
    print(s)

'''
Как доказать что это так?
'''
