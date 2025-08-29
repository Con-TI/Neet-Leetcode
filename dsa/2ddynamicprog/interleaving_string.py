class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # BIG NOTE: If you can create any interleaved string s3,
        # Then by default the sizes n and m are at most 1 different
        # Since by the pigeonhole principle any extras would have to merge
        # So we can focus solely on finding interleaving strings.
        # Idea: So long as we can start from the right or left end of s3
        # Then add letters one by one, then we can construct an interleaved string.

        if len(s1) + len(s2) != len(s3):
            return False
        
        # dp[i][j] represents whether s3[i+j:] can be 
        # formed by s1[i:] and s2[j:]
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        # Empty string base case
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
            
        return dp[0][0]
