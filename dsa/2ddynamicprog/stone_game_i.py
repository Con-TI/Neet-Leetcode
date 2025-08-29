class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Bottom up
        n = len(piles)
        # dp[i][j] represents the score alice gets considering piles from index i to j inclusive.
        dp = [[0] * n for _ in range(n)]

        for l in range(n-1, -1, -1):
            for r in range(l, n):
                even = (r-l) % 2 == 0
                left = piles[l] if even else 0
                right = piles[r] if even else 0
                if l == r:
                    dp[l][r] = left
                else:
                    dp[l][r] = max(dp[l + 1][r] + left, dp[l][r - 1] + right)
        
        total = sum(piles)
        alice_score = dp[0][n-1]
        return alice_score > total - alice_score