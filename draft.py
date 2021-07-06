n = 5
points = [[1, 1], [2, 2], [3, 3], [4, 4], [-1, -1]]
k = 3

ans = []
dist = [0]*len(points)

for i in range(len(points)):
    dist[i] = (points[i][0]*points[i][0] + points[i][1]*points[i][1])**0.5

print(dist)
print(points)

for i in range(0, len(dist)):
    for j in range(i, len(dist)):
        if dist[i] < dist[j]:
            dist[i], dist[j] = dist[j], dist[i]
            points[i], points[j] = points[j], points[i]

print(dist)
print(points)

for i in range(len(points)-1, -1, -1):
    if k > 0:
        print(*points[i])
        k -= 1

#использовать dict для расстояний, где расстояния это ключи
#сортировать по расстоянию 
