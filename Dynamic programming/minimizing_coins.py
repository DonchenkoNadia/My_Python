# n монет  https://cses.fi/problemset/task/1634
# каждая iая из которых имеет стоимость p[i] > 0
# дано число n
# минимальное количество монет которыми можно разменять сумму m
'''
1) пытаемся определить что такое d[j]
2) пытаемся составить переходы
3) пытаемся определить базу
4) фиксируем в каком элементе будет хранится ответ


d[j] = min (d[j-p[i]] + 1), i - 0..n-1 пробегаем по всем монетам, пытаемся найти минимальную сумму и говорим, что будет +1 монета

d[0] = 0
если j < 0, то ответ бесконечность, чтобы заведомо не взяли.
ответ в d[m]

d[j] = min(d[j-p[i]] + 1)

min = INF
for i in range (0, m):
    if d[j-p[i] < min:
        min = d[j-p[i])

d[j] = min + 1

'''
import math

sum = 11

dp = [math.inf for k in range(0, sum+1)]
dp[0] = 0

p = [1, 5, 7]

for i in range(1, sum+1):
    for j in range(0, len(p)):
        if (i - p[j]) >= 0:
            dp[i] = min(dp[i], dp[i - p[j]] + 1)

print(dp)
print(dp[sum])
