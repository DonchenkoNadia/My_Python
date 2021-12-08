nums = [-1,2,1,-4]
target = 1
nums.sort()
print(nums)
ans = 0
for i in range(0, len(nums)): # i = 0
    lo = i + 1 #
    hi = len(nums) - 1
    while lo < hi:
        if nums[i] + nums[lo] + nums[hi] == target:
            print("Here we are")
            print(target)
        if nums[i] + nums[lo] + nums[hi] < target:
            lo += 1
        if nums[i] + nums[lo] + nums[hi] > target:
            hi -= 1
        ans = min(ans, abs(target - (nums[i] + nums[lo] + nums[hi])))

print(ans)
