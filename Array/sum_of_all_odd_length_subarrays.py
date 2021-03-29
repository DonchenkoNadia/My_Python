class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        sum = 0
        i = 0
        while i <= len(arr):
            j = i
            while j <= len(arr):
                k = i
                if (j - k) % 2 == 1:
                    while k < j:
                        sum += arr[k]
                        k += 1
                j += 1
            i += 1
        return sum
"""
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        for i in range(len(arr)):
            for j in range(i,len(arr),2):
                ans += sum(arr[i:j+1])
        return ans
"""        
