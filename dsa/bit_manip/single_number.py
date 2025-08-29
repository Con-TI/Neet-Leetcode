class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # Idea: assign each num to a bit
        # At every addition of a new num, check if we have a match
        
        res = 0
        for num in nums:
            # Does xor with every number
            res ^= num
        # Since all duplicates will cancel themselves,
        # all that is left is the bit of the non duplicate
        return res