mat = [[10, 20, 46, 75, 94],       [11, 23, 48, 81, 95],       [13, 25, 49, 82, 97],       [15, 27, 52, 93, 98],       [16, 28, 55, 98, 99]]

val = 27
n = len(mat)

left = 0
right = n - 1

while left < right:
    mid = left + (right - left)//2
    if mat[mid][mid] > val:
        right = mid
    else:
        left = mid + 1
print(left)
print(mat[left-1][left-1])
print(mat[left][left])
