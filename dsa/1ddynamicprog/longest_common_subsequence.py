class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Bottom up
        """
        m,n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if text1[i] == text2[j]:
                    # Unlike most cases, we consider using a diagonal move
                    # if i and j are identical, then the longest common
                    # subsequence between text1[i:] and text2[j:] is just
                    # lcs(text[i+1:] and text[j+1:]) + 1
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    # The longest lcs of text1[i:] and text2[j:] 
                    # is either the same as i,j+1 or i+1,j.
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])

        return dp[0][0]
        """
        # Space optimized
        if len(text1) < len(text2):
            text1 , text2 = text2, text1
        
        # Prev represents row below
        # Curr represents row being computed
        prev = [0] * (len(text2) + 1)
        curr = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1 ,-1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    curr[j] = 1 + prev[j+1]
                else:
                    curr[j] = max(curr[j+1], prev[j])
            # Curr becomes prev for the next loop
            prev, curr = curr, prev

        return prev[0]