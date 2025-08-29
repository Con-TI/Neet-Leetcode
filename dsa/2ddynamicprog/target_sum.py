class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Bottom up
        n = len(nums)
        # dp[i][j] denotes the number of ways to get to j
        # using elements up to nums[:i]
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
                dp[i+1][total + nums[i]] += count
                dp[i+1][total - nums[i]] += count

        return dp[n][target]

        # Space optimized (Just replace having a matrix)
        # To having two rows to update (prev and next)
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            next_dp = defaultdict(int)
            for total,count in dp.items():
                next_dp[total + num] += count
                next_dp[total - num] += count
            dp[next_dp]
        return dp[target]