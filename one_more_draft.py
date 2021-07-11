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

s = "ababbababa"
t = "aba"
s1 = t + "#" + s
print(prefix(s1))
pi = prefix(s1)
print(pi[len(t)+1:])
print("   ")
ans = []
for i in range(len(t)+1, len(pi)):
    if pi[i] == len(t):
        ans.append(i-len(t)*2)
print(ans)

'''
аккуратно работаем с индексами и находим значения длины искомой строки.
Позиции на которых она встречается и есть начало вхождения.
Важно! искомый кусок ставим в начало, потом # потом строку, в которой ищем

'''
