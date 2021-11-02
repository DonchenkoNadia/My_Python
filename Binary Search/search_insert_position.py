'''
Given a sorted array of distinct integers and a target value,
return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

'''

class Solution:
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums)
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l

nums = [1,3,5,6]
target = 5
sol = Solution()

print(f"You schould insert your target = {target} at the position {sol.searchInsert(nums, target)}")
