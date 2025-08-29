class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Idea: The problem is asking to partition the stones into 
        # S1 and S2 to minimize |S1 - S2|.
        # So we treat this as a knapsack problem 
        # where instead of maximizing/minimizing, 
        # we look at getting as close to target as possible


        stoneSum = sum(stones)
        target = stoneSum // 2
        n = len(stones)

        dp = [[0] * (target + 1) for _ in range(n+1)]

        # i denotes using stones[:i]
        for i in range(1, n + 1):
            for t in range(target + 1):
                # If the target exceeds the weight of stone i
                # We try including vs not including into the weight
                if t >= stones[i-1]:
                    dp[i][t] = max(dp[i-1][t], stones[i-1] + dp[i-1][t-stones[i-1]])
                else:
                    # Otherwise we can't add the stone, 
                    # So the best score is the same as considering stones[:i-1]
                    dp[i][t] = dp[i-1][t]

        # Return smallest weight of left stone
        return stoneSum - 2*dp[n][target]