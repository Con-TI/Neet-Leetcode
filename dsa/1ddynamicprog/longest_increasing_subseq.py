class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Top down dp
        n = len(nums)
        dp = [-1] * n
        def dfs(i):
            if dp[i] != -1:
                return dp[i]
            
            res = 1
            for j in range(i+1,n):
                if nums[i] < nums[j]:
                    res = max(res, 1 + dfs(j))
            
            dp[i] = res
            return res
        return max(dfs(i) for i in range(n))

        # Bottom up dp
        n = len(nums)
        dp = [1] * n # Length of longest subarray starting from index i
        # left ptr i right ptr j
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
    
        return max(dp)