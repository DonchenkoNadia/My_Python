nums = [-1,2,1,-4]
target = 1
cur_delta = 0
cur_min_sum = 0
for i in range(0, len(nums)-1):
    for j in range(i, len(nums)-1):
        for k in range(j, len(nums)-1):
            cur_min_sum = nums[i] + nums[j] + nums[k]
            
