class Solution:
    def countSubstrings(self, s: str) -> int:
        # Dynamic programming
        """
        n = len(s)
        count = 0
        dp = [[False] * n for _ in range(n)]
        # Since we try to check the inner substring
        # we need to start i from n-1 instead of 0
        for i in range(n-1, -1, -1):
            for j in range(i,n):
                if s[i]==s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    count += 1
        return count
        """
        # Two ptr
        n = len(s)
        count = 0
        for i in range(n):
            # Odd
            l = i
            r = i
            while l >-1 and r < n and s[l] == s[r]:
                count += 1
                l-=1
                r+=1
        
            # Even
            l = i
            r = i+1
            while l >-1 and r < n and s[l] == s[r]:
                count += 1
                l-=1
                r+=1
        return count
            