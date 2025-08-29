class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        new_nums = [1] + nums + [1]
        # n+2 is length of padded array
        # dp[i][j] denotes the best score considering nums[i:j+1]
        dp = [[0] * (n+2) for _ in range(n+2)]
        

        for l in range(n, 0, -1):
            for r in range(l, n + 1):
                # Fix the last balloon i that will pop
                # Try all possible i
                for i in range(l, r + 1):
                    coins = new_nums[l-1]*new_nums[i]*new_nums[r+1]
                    coins += dp[l][i-1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[1][n]