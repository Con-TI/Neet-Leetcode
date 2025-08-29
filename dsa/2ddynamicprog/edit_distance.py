class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Bottom up
        # Goal: Find the least number of moves to get the words equal

        # Defaults to infinite
        # dp[i][j] is the num of ways considering word1[i:] and word2[j:]
        dp = [[float('inf')] * (len(word2) + 1) for i in range(len(word1) + 1)]
        
        # Defaults to deleting every letter
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j

        # Defaults to deleting every letter
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) -1, -1, -1):

                # If letters are identical, then equal to just considering i+1, j+1
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                # Minimum between the 3 moves (delete word1[i], insert word2[j], replace in that order)
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

        return dp[0][0]