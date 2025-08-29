class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        # Bottom up
        n = len(nums)
        # Memo of whether you can reach index n-1 from i
        dp = [False] * n
        dp[-1] = True
        for i in range(n-2, -1, -1):
            # Jump range
            end = min(n, i + nums[i] + 1)
            # Check all jump lengths
            for j in range(i + 1, end):
                if dp[j]:
                    dp[i] = True
                    break
        return dp[0]"""

        # Greedy
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
