class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder =  1

        for i in range(len(digits)-1, -1, -1):
            value = (digits[i] + remainder) % 10
            remainder = (digits[i] + remainder) // 10
            digits[i] = value

        if remainder == 1:
            digits.insert(0, 1)

        return digits
        
