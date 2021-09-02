#https://acmp.ru/asp/do/index.asp?main=task&id_course=3&id_section=23&id_topic=110&id_problem=618
a = [4, -5, 2, 5, -6, 8, 4, -9, 13, 0, 8, -13, -5, 20, -2]
n = len(a)

dp = [0 for i in range(0, n+1)]

dp[0] = a[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + a[i], a[i])

ans = dp[0]

for j in range(1, n):
    if dp[j] > ans:
        ans = dp[j]
        
print(dp)
print(ans)
