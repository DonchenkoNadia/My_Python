word1 = "honda"
word2 = "hyundai"

n = len(word1)
m = len(word2)

dp = [[0 for i in range(m+1)] for j in range(n+1)]


for i in range(n+1):
    dp[i][0] = i

for j in range(m+1):
    dp[0][j] = j

for k in range(len(dp)):
    print(dp[k])
print(" ")

for i in range(1, n + 1):
    for j in range(1, m + 1):
        left = dp[i - 1][j] + 1
        down = dp[i][j - 1] + 1
        diagonal =  dp[i - 1][j - 1]
        if word1[i - 1] != word2[j - 1]:
            diagonal += 1
        dp[i][j] = min(left, down, diagonal)

for k in range(len(dp)):
    print(dp[k])

print(f"answer is {dp[n][m]}")

for i in range(n, 0, -1):
    for j in range(m, 0, -1):
        if word1[i-1] == word2[j-1]:
            continue
        if dp[i][j] == dp[i-1][j-1] + 1:
            print(f"Edit {word2[j-1]} in {word2} to {word1[i-1]} in {word1}")
