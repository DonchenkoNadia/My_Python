#https://codeforces.com/problemset/problem/237/A?locale=en
n = int(input())
time = []
for i in range(0, n):
    time.append(list(map(int, input().split())))
    
ans = 1

for i in range(1, n):
    if (time[i][0] == time[i-1][0]):
        diff = abs(time[i][1] - time[i-1][1])
        if abs(diff) <= 1:
            ans += 1
    elif  (time[i][0] - time[i-1][0] == 1) and (time[i-1][1] == 59 and time[i][1] == 0):
        ans += 1

print(ans)
