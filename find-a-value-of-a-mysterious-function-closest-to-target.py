arr = [9,12,3,7,15]
target = 5

arr.sort()
print(arr)

def targetSearch(arr):
    l = 0
    r = len(arr)

    while l < r:
        mid = l + (r - l)//2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            r = mid
        else:
            l = mid + 1
    return l

print(arr[targetSearch(arr)])
