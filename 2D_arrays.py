#good example of working with matrix is task 200. Number of Islands
grid = [["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]]

def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
        return 0

    grid[i][j] = '0'

    dfs(grid, i + 1, j)
    dfs(grid, i - 1, j)
    dfs(grid, i, j + 1)
    dfs(grid, i, j - 1)

    return 1

if grid == None or len(grid) == 0:
    print("very bad")

numIslands = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '1':
            numIslands += dfs(grid, i, j)

print("Number of Islands: ", numIslands)
