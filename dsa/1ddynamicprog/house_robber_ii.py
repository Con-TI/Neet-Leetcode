class Solution:
    def rob(self, nums: List[int]) -> int:
        # Top down
        """
        if len(nums) == 1:
            return nums[0]
        
        # Array storing the vals for including and not including nums[0]
        memo = [[-1] * 2 for _ in range(len(nums))]
        def dfs(i,flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            if memo[i][flag] != -1:
                return memo[i][flag]
            memo[i][flag] = max(dfs(i+1, flag), nums[i] + dfs(i+2, flag))
            return memo[i][flag]
        return max(dfs(0, True), dfs(1, False))
        """

        # Bottom up
        """
        if len(nums) == 1:
            return nums[0]
        # Cutoff to make it a linear case instead of circular
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        """

        # Space optimized
        rob1, rob2 = 0,0
        for num in nums[:-1]:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp

        rob3, rob4 = 0,0
        for num in nums[1:]:
            temp = max(num + rob3, rob4)
            rob3 = rob4
            rob4 = temp
        return max(nums[0], rob2, rob4)

    def helper(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return dp[-1]