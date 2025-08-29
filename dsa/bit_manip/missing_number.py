class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        bit = 0
        for num in nums:
            bit |= (1<<num)

        res = (1 << (len(nums)+1)) - 1
        res ^= bit
        
        idx = -1
        while res:
            res = res >> 1
            idx += 1
        return idx
