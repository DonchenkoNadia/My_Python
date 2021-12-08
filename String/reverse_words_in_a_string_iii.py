grid = [[2,1,1],
        [1,1,0],
        [0,1,1]]

seen = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

print(seen)

def bfs(i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return False
    if seen[i][j] == 1:
        return False
    if i + 1 < len(grid)
    return True

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 2:
            if bfs(i, j):
                seen[i][j] == 1
