class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # Backtracking (Goes through all subsets in a backtracking manner
        # by popping from the subset once the subset is full
        # E.g. explores in this sequence: [], [1], [1,2], [2]
        res = 0
        def backtrack(i, subset):
            nonlocal res
            # Identity property of XOR allows us to start with xorr = 0
            # 0 ^ a = a for all a.
            xorr = 0
            for num in subset:
                # XOR Operator on each num in a subset
                xorr ^= num
            # Add XOR of subset
            res += xorr
        
            # Generates all subsets and runs them
            for j in range(i, len(nums)):
                subset.append(nums[j])
                # Re-run backtrack (using j+1 prevents double counting)
                backtrack(j+1, subset)
                subset.pop()
            
        backtrack(0, [])
        return res

        # Bit manipulation 
        # (Builds up a list of all bits that are hit and does bitshift)
        # Works since every bit contributes to half of the XOR sums
        # This is because every XOR will have either an even or odd
        # number of nums with the kth bit = 1, so half.

        res = 0
        for num in nums:
            res |= num
        return res << (len(nums) - 1)