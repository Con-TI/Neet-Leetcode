class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits.reverse()

        i = 0
        while i < len(digits) and digits[i] + 1 > 9:
            digits[i] = 0
            i += 1

        if i == len(digits):
            digits.append(0)
        digits[i] += 1
        digits.reverse()
        return digits