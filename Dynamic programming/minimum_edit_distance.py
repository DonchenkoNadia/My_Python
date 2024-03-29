https://www.youtube.com/watch?v=We3YDTzNXEk&t=469s
word1 = "abcdef"
word2 = "azced"
n = len(word1)
m = len(word2)

# if one of the strings is empty
#if n * m == 0:
#    return n + m

# array to store the convertion history
d = [ [0] * (m + 1) for _ in range(n + 1)]

# init boundaries
for i in range(n + 1):
    d[i][0] = i
for j in range(m + 1):
    d[0][j] = j

# DP compute
for i in range(1, n + 1):
    for j in range(1, m + 1):
        left = d[i - 1][j] + 1
        down = d[i][j - 1] + 1
        left_down = d[i - 1][j - 1]
        if word1[i - 1] != word2[j - 1]:
            left_down += 1
        d[i][j] = min(left, down, left_down)

#return d[n][m]

for i in range(len(d)):
    print(d[i])

print(f"result = {d[n][m]}")
