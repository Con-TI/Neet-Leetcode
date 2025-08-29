class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Bottom up
        m,n = len(grid), len(grid[0])
        dp = [[0]*(n+1) for _ in range(m+1)]

        dp[m-1][n-1] = grid[m-1][n-1]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                if i == m-1:
                    dp[i][j] = dp[i][j+1] + grid[i][j]
                    continue
                if j == n-1:
                    dp[i][j] = dp[i+1][j] + grid[i][j]
                    continue
                dp[i][j] = grid[i][j] + min(dp[i][j+1],dp[i+1][j])

        return dp[0][0]
