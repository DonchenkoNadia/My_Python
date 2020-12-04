height = [4,2,0,3,2,5]
res = 0
level = 0
l = 0
r = len(height) - 1
if height == None or len(height) == 0:
    res = 0
    #return 0
while l < r:
    if height[l] < height[r]:
        lower = height[l]
        l += 1
    else:
        lower = height[r]
        r -= 1
    level = max(level, lower)
    res = res + (level - lower)

print ("Trap: ", res)
