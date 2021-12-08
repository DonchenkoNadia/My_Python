mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]

def line_bin_search(mat):
    l = 0
    r = len(mat) - 1
    ans = -1

    while l <= r:
        mid = l + (r - l)//2

        if mat[mid] == 1:
            ans = mid
            break

        if mat[mid] == 0:
            l = mid + 1
        else:
            r = mid - 1

    return ans

min_ = 101

for i in mat:
    res = line_bin_search(i)
    min_ = min(res, min_)


print(min_)
