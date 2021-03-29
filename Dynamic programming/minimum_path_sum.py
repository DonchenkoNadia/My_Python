class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)     #number of rows
        n = len(grid[0])  #number of columns

        if m == 1 and n == 1:
            #return grid[0][0]
            print (grid[0][0])

        if m == 0 or n == 0:
            #return 0
            print (0)

        costs = [[1 for x in range(n)] for x in range(m)]
        costs[0][0] = grid[0][0]

        for i in range (1, n):
            costs[0][i] = grid[0][i] + costs[0][i-1]

        for i in range (1, m):
            costs[i][0] = grid[i][0] + costs[i-1][0]

        for i in range(1, m):
            for j in range(1, n):
                costs[i][j] = grid[i][j] + min(costs[i-1][j], costs[i][j-1])

        return costs[-1][-1]
