'''
Даны числа m * n
Построить граф

4 - 7 - 2
|   |   |
3 - 0 - 6
|   |   |
5 - 1 - 8

0 - 1
|   |
2 - 3
|   |
4 - 5

m - number of rows
n - number of columns
'''

def buildGraph(m, n):
    grid = {}
    for i in range(m*n-1):
        grid.append(i, i+1)
        


    return grid

m = 3
n = 3
print(buildGraph(m, n))
