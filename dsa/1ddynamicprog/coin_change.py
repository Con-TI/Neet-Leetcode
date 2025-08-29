class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Stores the number of coins to get to amount i
        if amount in coins:
            return 1
        if amount == 0:
            return 0
        if (amount < min(coins)):
            return -1

        dp = [-1] * (amount+1)
        for coin in coins:
            if coin < amount:
                dp[coin] = 1

        # Bottom up
        for i in range(min(coins)+1, amount+1):
            if i not in coins:
                possibilities = [dp[i-j]+1 for j in coins if ((i-j > 0) and dp[i-j]!=-1)]
                if possibilities:
                    dp[i] = min(possibilities)

        return dp[amount]

        # Bottom up (from solutions)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1