class Solution:
    def integerBreak(self, n: int) -> int:
        # Bottom up
        dp = [0] * (n + 1)
        dp[1] = 1
        for num in range(2, n+1):
            # Take into account that we need to consider one element
            # sums if num < n since we can have, for example (n-1) * 1 as a product
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                dp[num] = max(dp[num], dp[i]*dp[num-i])
        return dp[n]

        # Math (Based on the idea that 3 is the best number to increment/multiply by)
        if n<=3:
            return n-1
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n