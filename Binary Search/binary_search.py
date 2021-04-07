class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        pivot = 0
        while left <= right:
            pivot = left + (right -  left)  // 2
            if nums[pivot] == target:
                return pivot
            elif target < nums[pivot]:
                right = pivot - 1
            elif target > nums[pivot]:
                left = pivot + 1
        return -1
