from heapq import *
'''
minHeap = []

nums = [3, 1, 5, 12, 2, 11]
k = 3

for i in range(len(nums)):
    heappush(minHeap, nums[i])

print(minHeap)
for i in range(len(minHeap)):
    print(heappop(minHeap))
'''
arr = [3,3,3,3,5,5,5,2,2,7]
dict = {}
for i in arr:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)
l = list(dict.values())
print(l)
print(heapify(l))

total_removed = 0
ans = 0
while l:
    total_removed += heappop(l)
    print(total_removed)
    ans += 1
    if tot
print(ans)
