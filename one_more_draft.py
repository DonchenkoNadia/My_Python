field = [[2, 1, 1],
         [2, 1, 1],
         [2, 2, 2]]

res = 0
path = []

res = field[0][0]
path.append([0,0])

for i in range(1, len(field)):
    for j in range(1, len(field[0])):
        res = res + max(field[i-1][j], field[i][j-1])
        if field[i-1][j] > field[i][j-1]:
            path.append([i-1, j])
        else:
            path.append([i, j-1])
print(res)
print(path)
