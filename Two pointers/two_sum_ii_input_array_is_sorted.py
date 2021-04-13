class Solution:
    def twoSum(self, numbers, target):
        low = 0
        high = len(numbers) - 1
        while low < high:
            sum_ = numbers[low] + numbers[high]
            if sum_ == target:
                return [low + 1, high + 1]
            elif sum_ < target:
                low += 1
            else:
                high -= 1
        return [-1, -1]
sol = Solution()
numbers = [2,7,11,15]
target = 9
print(sol.twoSum(numbers, target))
