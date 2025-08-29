class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Top down approach
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1] * n for _ in range(m+1)]
        dp[m-1][n-1] = 1

        # Here we build up from scratch with no accumulation
        def dfs(i,j):
            if i>=m or j>=n or obstacleGrid[i][j]:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = dfs(i+1,j) + dfs(i,j+1)
            return dp[i][j]

        return dfs(0,0)
        """

        # Bottom up approach
        """
        m,n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n+1) for _ in range(m+1) ]
        dp[m-1][n-1] = 1
        print(dp)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                # += here accounts for the base case of 1
                dp[i][j] += dp[i+1][j] + dp[i][j+1]
            
        return dp[0][0]
        """

        # In place approach
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0

        obstacleGrid[m-1][n-1] = 1
        for r in range(m-1,-1,-1):
            for c in range(n-1, -1, -1):
                if r == m - 1 and c == n - 1:
                    continue

                if obstacleGrid[r][c] == 1:
                    obstacleGrid[r][c] = 0
                else:
                    down = obstacleGrid[r + 1][c] if r + 1 < m else 0
                    right = obstacleGrid[r][c + 1] if c + 1 < n else 0
                    obstacleGrid[r][c] = down + right

        return obstacleGrid[0][0]