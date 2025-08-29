class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Bottom up
        n = len(nums)
        # dp[i][1] max subarray sum starting at index i
        # dp[i][0] max subarray sum starting at or after index i

        dp = [[0] * 2 for _ in range(n)]
        dp[n-1][1] = dp[n-1][0] = nums[n-1]
        for i in range(n-2, -1, -1):
            # Reset or extend
            dp[i][1] = max(nums[i], nums[i] + dp[i+1][1])
            
            # Best so far
            dp[i][0] = max(dp[i+1][0], dp[i][1])
        
        # Best starting from 0 or after.
        return dp[0][0]

        # Kadane's 
        maxSub, curSum = nums[0], 0
        for num in nums:
            # Idea: reset if curSum < 0 since its better to discard it.
            # maxSub will keep track of the best subarray so far.
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub