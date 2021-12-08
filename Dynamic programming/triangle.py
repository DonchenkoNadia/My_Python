n = 5
k = 3
fence = [0 for i in range(0, n)]
res = [0 for i in range(0, k)]
friends = [[1, 3, 4], [2, 4, 5], [3, 2, 3], [1, 5, 5]]

for friend in friends:
    color = friend[0]
    start = friend[1]
    end = friend[2]
    for j in range(start-1, end):
        fence[j] = color

print(fence)
for i in range(n):
    if fence[i] > 0:
        res[fence[i]-1] +=1
print(res) 
