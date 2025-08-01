"""
You are given an array nums, that might contain duplicates , return all possible unique permutations in any order.
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # Backtracking algorithm (works through swapping in-place)
        res = []
        def backtrack(i):
            # Arranges things in place
            if i == len(nums):
                res.append(nums[:])
                return
        
            for j in range(i,len(nums)):
                # Don't swap identical entries
                if j>i and nums[i] == nums[j]:
                    continue

                # Swap them
                nums[i], nums[j] = nums[j], nums[i]
                # Backtrack now
                backtrack(i+1)
            
            # Allows for proper backtracking since we are swapping in place 
            # so we'd need to revert in bulk all the swaps that occured.
            for j in range(len(nums)-1, i, -1):
                nums[j], nums[i] = nums[i], nums[j]
        
        nums.sort()
        backtrack(0)
        # Note first perm in res is always sorted nums itself from the algo.
        return res
