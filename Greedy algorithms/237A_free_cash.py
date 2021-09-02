#https://codeforces.com/problemset/problem/237/A?locale=en
n = 3
time = [[0, 12], [10, 11], [22, 22]]

ans = 1

for i in range(1, n):
    if (time[i][0] == time[i-1][0]):
        diff = abs(time[i][1] - time[i-1][1])
        if abs(diff) <= 1:
            ans += 1
    elif  (time[i][0] - time[i-1][0] == 1) and (time[i-1][1] == 59 and time[i][1] == 0):
        ans += 1

print(ans)
