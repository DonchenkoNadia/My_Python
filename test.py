#graph = [[1, 2], [1, 3], [3, 4], [3, 5]]
graph = [[1, 2], [3, 3]]
dict = {}
#добавили все существующие вершины в словарь
for i in range(len(graph)):
    if graph[i][0] not in dict:
        dict[graph[i][0]] = 0
    if graph[i][1] not in dict:
        dict[graph[i][1]] = 0
print(dict)

#для каждой вершины делает поиск
for i, v in dict.items():
    print(i)

def isConnected(dict):
    for i in dict:
        if dict[i] < 1:
            return 0
    return 1

if isConnected(dict):
    print("Is connected :)")
else:
    print("Is not connected")
