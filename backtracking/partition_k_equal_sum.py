class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # subset sum partition
        
        # Backtracking (Brute/going through everything)
        # if sum(nums)%k != 0:
        #     return False

        # nums.sort(reverse=True)
        # target = sum(nums) // k
        # used = [False] * len(nums)

        # def backtrack(i, k, subsetSum):
        #     # We've gone through all the subsets needed
        #     if k == 0:
        #         return True

        #     if subsetSum == target:
        #         # Move on to trying to make the next subset with the existing used
        #         return backtrack(0, k-1, 0)
        #     for j in range(i, len(nums)):
        #         # If j is already used or causes sum to exceed ski[]
        #         if used[j] or subsetSum + nums[j] > target:
        #             continue

        #         used[j] = True
        #         # Try seeing if there's a path after adding j to existing subset
        #         if backtrack(j+1, k, subsetSum + nums[j]):
        #             return True
                
        #         # Backtrack step on the used array
        #         used[j] = False
            
        #     # If nothing works, then return False on the current sub path
        #     return False
        
        # return backtrack(0,k,0)

        # Backtracking with pruning step
        # total = sum(nums)
        # if total % k != 0:
        #     return False

        # nums.sort(reverse = True)
        # target = total // k
        # used = [False] * len(nums)

        # def backtrack(i, k, subsetSum):
        #     if k == 0:
        #         return True
        #     if subsetSum == target:
        #         return backtrack(0, k-1, 0)

        #     for j in range(i, len(nums)):
        #         if used[j] or subsetSum + nums[j] > target:
        #             continue
        #         used[j] = True
        #         if backtrack(j + 1, k, subsetSum + nums[j]):
        #             return True
        #         used[j] = False

        #         # Pruning step since 
        #         # - there is too large a number in nums
        #         # - the current path fails, and since every
        #         # subsequent number in nums is smaller by the 
        #         # initial sorting, we can safely ignore them
        #         if subsetSum == 0:
        #             return False
            
        #     return False

        # return backtrack(0, k, 0)

        # Backtracking with bit masking and pruning
        # Using a mask over an array of used/unused keeps space constant
        # However this will only work with sufficiently small n
        # Python can use arbitrarily large 2^n but the computation and 
        # memory will explode instead of staying constant once n
        # exceeds something like 20
        """
        total = sum(nums)
        if total % k != 0:
            return False

        nums.sort(reverse = True)
        target = total // k
        n = len(nums)

        def backtrack(i, k, subsetSum, mask):
            if k == 0:
                return True
            
            if subsetSum == target:
                return backtrack(0, k - 1, 0, mask)
            
            for j in range(i,n):
                # If num j is not in the subset or subsetSum with j exceeds target skip
                if (mask & (1 << j)) == 0 or subsetSum + nums[j] > target:
                    continue
                # Continue with the jth turned off
                if backtrack(j+1, k, subsetSum + nums[j], mask ^ (1 << j)):
                    return True
                # Pruning step
                if subsetSum == 0:
                    return False
            return False

        # We start with mask with bits all 1. This represents everything being unused.
        return backtrack(0, k, 0, (1 << n) - 1)
        """

        # Top-down DP with bit mask
        # total = sum(nums)
        # if total % k != 0:
        #     return False
        
        # nums.sort(reverse=True)
        # target = total // k
        # n = len(nums)
        # dp = [None] * (1 << n)

        # def backtrack(i, k, subsetSum, mask):
        #     if dp[mask] != None:
        #         return dp[mask]
        #     if k == 0:
        #         dp[mask] = True
        #         return True
        #     if subsetSum == target:
        #         dp[mask] = backtrack(0, k-1,  0, mask)
        #         return dp[mask]
            
        #     for j in range(i,n):
        #         if (mask & (1 << j)) == 0 or subsetSum + nums[j] > target:
        #             continue
        #         if backtrack(j+1, k, subsetSum + nums[j], mask ^ (1<<j)):
        #             dp[mask] = True
        #             return True
        #         if subsetSum == 0:
        #             dp[mask] = False
        #             return dp[mask]
        #     dp[mask] = False
        #     return False
        
        # return backtrack(0, k, 0, (1<<n) - 1)

        # Bottom up DP with bit mask
        # Start from empty subset
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        n = len(nums)
        # 2^N
        N = 1 << n
        dp = [0] + [-1] * (N - 1)

        for mask in range(N):
            if dp[mask] == -1:
                continue
            for i in range(n):
                # If i is not in the subset and it can be added safely
                if (mask & (1 << i)) == 0 and dp[mask] + nums[i] <= target:
                    # Mark (mask | (1 << i)) which is the subset with i included
                    # as the current num
                    dp[mask | (1 << i)] = (dp[mask] + nums[i]) % target

        # See if the filled subset is valid
        return dp[N - 1] == 0
