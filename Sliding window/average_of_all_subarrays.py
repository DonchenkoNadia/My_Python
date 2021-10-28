nums = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
ans = []

for i in range(0, len(nums)-k+1):
    tmp = 0
    for j in range(i, i+k):
        tmp += nums[j]
    tmp /= k
    ans.append(tmp)

print(ans)

#Optimizing:
opt_ans = []
l = 0
r = k
windowSum = 0
for i in range(l, r):
    windowSum += nums[i]
opt_ans.append(windowSum / k)
print(opt_ans)

while r + 1 < len(nums):
    windowSum -= nums[l]
    l += 1
    r += 1
    tmp += nums[r]
    print(nums[r])
    opt_ans.append(tmp / k)

print(opt_ans)
