class Solution:
    def rob(self, nums: List[int]) -> int:
        # Top down
        """
        dp = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            dp[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return dp[i]
        
        return dfs(0)
        """
        
        # Bottom up
        """
        n = len(nums)
        if not nums:
            return 0
        
        if n == 1:
            return nums[0]
        # Idea: build up a cache of the max money possible in the sublist nums[:i]
        dp = [0] * n
        dp[0] = nums[0]
        # Either start at 0 or 1
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            # Either don't include i or include i
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        # Max money on the entire list
        return dp[n-1]
        """

        # Space optimized
        rob1, rob2 = 0,0
        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2