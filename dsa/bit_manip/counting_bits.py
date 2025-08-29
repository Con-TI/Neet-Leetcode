class Solution:
    def countBits(self, n: int) -> List[int]:
        # Basic
        res = []
        """
        for i in range(n+1):
            k = i
            ones = 0
            while k:
                if k % 2:
                    ones += 1
                k = k >> 1
            res.append(ones)
        return res
        """
        # Bit manipulation
        dp = [0] * (n+1)
        for i in range(n + 1):
            # Number of 1 bits in i 
            # is equal to number of 1 bits in right shifted
            # plus 1 if the last bit in i is 1
            dp[i] = dp[i >> 1] + (i & 1)
        return dp