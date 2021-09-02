#https://acmp.ru/?main=task&id_task=122
#a = [3, 29, 5, 5, 28, 6]
#n = len(a)

fin  = open("input.txt")
fout = open("output.txt","w")

n = int(fin.readline())
a = list(map(int,fin.readline().split()))


dp = [-1 for i in range(0, n+1)]
dp[0] = 1

#в массиве мы храним максимальную длину возрастающего
#поддотрезка до числа a[i]

for i in range(1, n):
    dp[i] = 1
    for j in range(0, i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], 1 + dp[j])

#print(dp)
ans = dp[0]

for j in range(1, n):
    if dp[j] > ans:
        ans = dp[j]

#print(ans)
fout.write(str(ans))

fin.close()
fout.close()
