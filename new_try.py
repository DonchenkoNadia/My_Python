fin  = open("input.txt")
fout = open("output.txt","w")
s = fin.readline()
#n = 2
n = int(s)
dp = [0 for i in range(0, n+1)]

dp[0] = 1
dp[1] = 3

for i in range(2, n+1):
    dp[i] = dp[i-1]*2

fout.write(str(dp[n]))

fin.close()
fout.close()
