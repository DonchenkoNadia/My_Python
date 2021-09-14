edges = [[1, 2], [2, 4], [2, 5], [1, 3], [3, 6], [3, 7], [1, 9]]
graph = {}
root = 1
for x, y in edges:
    if x not in graph:
        graph[x] = []
    graph[x].append(y)

    if y not in graph:
        graph[y] = []
    graph[y].append(x)

def CheckIfBinary(graph):
    if len(graph[root]) > 2:
        return 0
    for i in graph.items():
        if len(i) > 3:
            return 0
    return 1

print(graph)

if CheckIfBinary(graph):
    print("Looks like binary tree!")
else:
    print("It is not a binary tree")
