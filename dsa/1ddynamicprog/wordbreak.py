class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Dynamic prog
        n = len(s)
        t = max([len(i) for i in wordDict])
        dp = [False] * n
        for i in range(n):
            if s[:i+1] in wordDict:
                dp[i] = True
                continue
            if s[i] in wordDict:
                dp[i] = dp[i-1]
                continue
            for j in range(t+1):
                if i-j >= 0:
                    if s[i-j:i+1] in wordDict:
                        dp[i] = dp[i-j-1]
        return dp[n-1]
