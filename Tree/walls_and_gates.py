from collections import deque

rooms = [[2147483647,-1,0,2147483647],
        [2147483647,2147483647,2147483647,-1],
        [2147483647,-1,2147483647,-1],
        [0,-1,2147483647,2147483647]]

queue = deque()
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

rows = len(rooms)
cols = len(rooms[0])

steps = 1

for r in range(rows):
    for c in range(cols):
        if rooms[r][c] == 0:
            queue.append((r, c))

queue.append((-1, -1)) #impossible indexes values as a level marker

while queue:
    row, col = queue.popleft()
    '''
    if row == -1: #time to make a step
        steps += 1
        if queue:
            queue.append((-1, -1))
    else:
        #trying to move
        for d in directions:
            neighbor_row = row + d[0]
            neighbor_col = col + d[1]
            if rows > neighbor_row >= 0 and cols > neighbor_col >= 0:
                if rooms[neighbor_row][neighbor_col] != -1 and rooms[neighbor_row][neighbor_col] != 0:
                    rooms[neighbor_row][neighbor_col] = min(rooms[neighbor_row][neighbor_col], steps)
                    queue.append((neighbor_row, neighbor_col))
    '''
print(rooms)
