class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Idea: Keep track of whether you can reach sums up to target
        # using the first i nums
        # Bottom up         
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n+1)]
        # Denote i j true if you can reach sum j from the first i nums.
        # Mark the zeroes
        for i in range(n+1):
            dp[i][0] = True
        
        for i in range(1, n + 1):
            for j in range(1, target + 1):
                # Include nums[i-1] if it is less than j
                if nums[i-1] <= j:
                    # Check if you can get j with the first i-1 elements
                    # Or if you can get j-nums[i-1] if you include nums[i-1]
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    # Check if you can get j with the first i-1 elements
                    dp[i][j] = dp[i-1][j]

        # If you can achieve target with the first n elements (any of them)
        # Then it automatically implies you can reach target with the rest.
        return dp[n][target]
        """
        
        # Top down
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)
        # dp[i][j] represents whether you can achieve j using nums[i:]
        dp = [[-1] * (target + 1) for _ in range(n+1)]
        def dfs(i, target):
            if target == 0:
                return True
            if i >= n or target < 0:
                return False
            if dp[i][target] != -1:
                return dp[i][target]
            
            dp[i][target] = (dfs(i+1,target)) or dfs(i+1, target - nums[i])
            return dp[i][target]
        
        return dfs(0, target)
        """
        
        # DP optimal
        """
        if sum(nums) % 2:
            return False
        
        target = sum(nums) // 2
        # Keeps track of which sums j are achievable
        dp = [False] * (target + 1)
        # Null sum achievable
        dp[0] = True


        for num in nums:
            for j in range(target, num - 1, -1):
                # If its already updated dp[j]
                # dp[j - num]
                dp[j] = dp[j] or dp[j - num]
        
        return dp[target]
        """

        # DP Bitset
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total//2
        dp = 1 << 0
        # if bit j is 1, that means a subset exists that sums to j
        for num in nums:
            # Or operator with bitshift by num to 
            # form a new num with preexisting bits j and j+num set to 1
            dp |= dp << num

        # And operator to check if "target"th bit is set to 1
        return (dp & (1<< target)) != 0