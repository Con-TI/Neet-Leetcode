class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # Number of stones
        n = len(stoneValue)

        # dp[i] will store the best possible net score difference (Alice - Bob)
        # that the current player can guarantee starting from stone index i
        dp = [float('-inf')] * (n + 1)

        # Base case:
        # If there are no stones left to take (i == n), the net score difference is 0
        dp[n] = 0

        # Iterate backwards from the last stone to the first
        # This is a bottom-up DP approach
        for i in range(n - 1, -1, -1):
            total = 0  # Total value of stones taken in current move
            # Try taking 1, 2, or 3 stones (as allowed)
            for j in range(i, min(i + 3, n)):
                total += stoneValue[j]
                # The current player gains `total` immediately.
                # The opponent will start from index j+1, and their best net difference is dp[j+1]
                # So, the net gain for the current player is total - dp[j+1]
                # We want the maximum net gain possible
                dp[i] = max(dp[i], total - dp[j + 1])

        # At the end, dp[0] is the maximum net score difference Alice can guarantee if she starts the game
        result = dp[0]

        # If the score difference is 0, it's a tie
        if result == 0:
            return "Tie"
        # If the difference is positive, Alice wins
        elif result > 0:
            return "Alice"
        # Otherwise, Bob wins
        else:
            return "Bob"