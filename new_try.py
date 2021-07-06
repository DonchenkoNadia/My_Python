'''
”aabaababa”
 a - 0
 aa - 1
 aab - 0
 aaba - 1
 aabaa - 2
 aabaab - 3
 aabaaba - 4
 aabaabab - 0
 aabaababa - 1

 'aabaabaaaaba'
 a - 0
 aa - 1
 aab - 0
 aaba - 1
 aabaa - 2
 aabaab - 3
 aabaaba - 4
 aabaabaa - 5
 aabaabaaa - 2
 aabaabaaaa - 2
 aabaabaaaab - 3
 aabaabaaaaba - 4
'''

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

s = 'ABACABADABACABA'
print(prefix(s))

n = len(s)
pi = prefix(s)
k = n - pi[n-1]
print(k)
print(n % k)

if n % k == 0:
    print(s[0:k])
else:
    print(s)

'''
Как доказать что это так?
'''
