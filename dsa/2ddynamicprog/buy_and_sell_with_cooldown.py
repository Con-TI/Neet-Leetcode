class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Bottom up
        # You have two states, allowed to buy vs allowed to sell
        # State dp[i][buying]: max profit starting at day i
        # buying = True → you are allowed to buy
        # buying = False → you are holding a stock and can sell

        n = len(prices)
        dp = [[0]*2 for _ in range(n + 1)]

        # Work backwards considering snippet prices[i:]
        for i in range(n-1, -1, -1):
            for buying in [True, False]:
                if buying:
                    # Two choices:
                    # 1. Buy today → lose prices[i], then move to day i+1 in selling state
                    # 2. Skip buying → stay in buying state on day i+1
                    buy = dp[i+1][False] - prices[i] if i+1 < n else -prices[i]                     
                    cooldown = dp[i+1][True] if i+1 < n else 0
                    dp[i][True] = max(buy, cooldown)
                else:
                    # Two choices:
                    # 1. Sell today → gain prices[i], then move to day i+2 buying state
                    # 2. Skip selling → continue to day i+1 in selling state
                    sell = dp[i+2][True] + prices[i] if i+2 < n else prices[i]
                    cooldown = dp[i+1][False] if i+1 < n else 0
                    dp[i][False] = max(sell, cooldown)
  
        return dp[0][True]
