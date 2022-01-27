from collections import deque

ocean = [[0, 1, 1, 0, 1],
         [0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [1, 0, 0, 0, 1],
         [1, 0, 0, 0, 1]]
grid = [[0]*len(ocean[0])]*len(ocean)

directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
stack = deque(["a", "b", "c", "d", "e", "f"])

def dfs(i, j, ch):
    if i < 0 or i >= len(ocean) or j < 0 or j >= len(ocean[0]) or ocean[i][j] == 0:
        return 0
    ocean[i][j] = 0
    grid[i][j] = ch
    for row, col in directions:
        dfs(i+row, j+col, ch)
    return 1

ans = 0

for i in range(len(ocean)):
    for j in range(len(ocean[0])):
        if ocean[i][j] == 1 and stack:
            ans += dfs(i, j, stack.popleft())

print(f"Total numberr of islands is {ans}")

for row in grid:
    print(row)
