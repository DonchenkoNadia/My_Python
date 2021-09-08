isConnected = [[1, 1, 0],
               [1, 1, 0],
               [0, 0, 1]]

for i in range(len(isConnected)):
    for j in range(len(isConnected[i])):
        print(f"isConnected[{i}][{j}] = {isConnected[i][j]}")

root = [0 for i in range(len(isConnected[0]))]

for i in range(len(isConnected)):
    for j in range(len(isConnected[i])):
        if isConnected[i][j] == 1:
            root[j] = j

print(root)
