class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0
        m, n = len(s), len(t)
        # Number of ways s[i:] can form t[j:]
        dp = [[0] * (n+1) for _ in range(m+1)]

        # Default since t[n:] = ""
        for i in range(m+1):
            dp[i][n] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]

        return dp[0][0]

