class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # dp[i][j][k] denotes 
        # best score given piles[j:] and M=k
        # where i=0 denotes the opponent's target (minimizing your score) 
        # and i=1 denotes your target (maximizing your score)

        dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(2)]

        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):
                total = 0
                dp[1][i][M] = 0
                dp[0][i][M] = float("inf")

                for X in range(1, 2 * M + 1):
                    if i + X > n:
                        break
                    total += piles[i + X - 1]

                    # Player considers taking piles[i+x]
                    dp[1][i][M] = max(dp[1][i][M], total + dp[0][i + X][max(M, X)])
                    # Opponent considers making the player skip piles[i:x]
                    dp[0][i][M] = min(dp[0][i][M], dp[1][i + X][max(M, X)])

        return dp[1][0][1]