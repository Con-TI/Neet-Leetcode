class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Top down
        """
        dp = [[-1] * n for _ in range(m)]
        def dfs(i,j):
            if  i == (m - 1) and j == (n - 1):
                return 1
            if i >= m or j >= n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            dp[i][j] = dfs(i, j + 1) + dfs(i + 1, j)
            return dp[i][j]

        return dfs(0,0)
        """
        
        # Bottom up 
        # Number of ways to get from i,j to [n-1][m-1]
        """
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[m-1][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                # Either down or right
                dp[i][j] += dp[i+1][j] + dp[i][j+1]
        return dp[0][0]
        """

        # Space optimized
        # Essentially does the same thing but just maintains the running
        # row values
        # By the end the array has the values corresponding to dp[0][j]
        row = [1]*n
        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]
        
        # Maths ((n-1) right moves, (m-1) down moves)
        """
        if m == 1 or n == 1:
            return 1

        if m < n:
            m, n = n, m

        res = j = 1
        # (m-1)+(n-1) choose (m-1) 
        # = (m+n-2)*...*(m)/(1*2*...*n-1)
        for i in range(m, m + n - 1):
            res *= i
            res //= j
            j += 1

        return res
        """