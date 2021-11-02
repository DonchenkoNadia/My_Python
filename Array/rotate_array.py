class Solution:
    def rotate(self, nums, k):
        def reverse(a, b):
            if b > len(nums)-1:
                return
            l = a
            r = b
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        k = k % len(nums)

        reverse(0, len(nums)-1)

        reverse(0, k-1)

        reverse(k, len(nums)-1)

nums = [1,2,3,4,5,6,7]
k = 3
sol = Solution()
sol.rotate(nums, k)
print(f"answer is {nums}")
