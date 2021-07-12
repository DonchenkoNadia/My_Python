matrix = [[0, 0, 0, 1],
          [0, 0, 1, 0],
          [1, 0, 1, 0]]

new_matrix = []
new_matrix.append([0]*(len(matrix[0])+2))
for i in matrix:
    new_matrix.append([0]+i+[0])
new_matrix.append([0]*(len(matrix[0])+2))

print(new_matrix)
ans = 0
for i in range(1, len(new_matrix)):
    for j in range(1, len(new_matrix[0])):
        if new_matrix[i][j] == 1 and new_matrix[i-1][j] == 0 and new_matrix[i+1][j] == 0 and new_matrix[i][j-1] == 0 and new_matrix[i][j+1] == 0:
            ans += 1
            new_matrix[i][j] == 0
print(ans)
