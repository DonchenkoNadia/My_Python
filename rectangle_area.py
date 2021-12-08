rect = [
    [4, 4, 5, 6],
    [2, 2, 3, 3],
    [3, 3, 4, 4]
]

for i in range(1, len(rect)):
    Cx = min(rect[i][0], rect[i-1][0])
    Cy = min(rect[i][1], rect[i-1][0])
    Dx = max(rect[i][2], rect[i-1][2])
    Dy = max(rect[i][3], rect[i-1][3])

def CheckIfPointInside(x, y):
    for i in range(len(rect)):
        if x >= rect[i][0] and y >= rect[i][1] and x < rect[i][2] and y < rect[i][3]:
            return True
    return False

#[[x1, y1, x2, y2],...[x1, y1, x2, y2]]

ans = 0

for y in range(Cy, Dy+1):
    for x in range(Cx, Dx+1):
        print (f"x = {x}, y = {y}")
        if CheckIfPointInside(x, y):
            ans += 1
            print ("point added")
print(ans)
