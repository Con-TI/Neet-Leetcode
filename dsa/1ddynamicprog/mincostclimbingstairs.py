class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Top down
        # Keep track of minimum cost from a step to the top
        """
        n = len(cost)
        dp = [-1] * n
        def dfs(i):
            if i>=n:
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] =  cost[i] + min(dfs(i+1), dfs(i+2))
            return dp[i]
        return min(dfs(0), dfs(1))
        """

        # Bottom up
        # Keep track of minimum cost from a step to the top
        """
        n = len(cost)
        dp = [-1] * (n + 1)
        dp[1], dp[2] = cost[n-1], cost[n-2]
        for i in range(3,n+1):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[n-i]
        return min(dp[n-1],dp[n])
        """
        # Space optimized
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])