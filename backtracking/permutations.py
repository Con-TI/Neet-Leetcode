class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums: List[int], idx:int):
        # Optimal backtrack (avoids iterating through already seen things
        # without checking an if statement)
        if idx == len(nums):
            self.res.append(nums[:])
            return
        for i in range(idx, len(nums)):
            nums[idx], nums[i] = nums[i], nums[idx]
            self.backtrack(nums, idx+1)
            nums[idx], nums[i] = nums[i], nums[idx]


    # def permute(self, nums: List[int]) -> List[List[int]]:
    #     n =  len(nums)
    #     res = []

    #     def backtrack(subset):
    #         nonlocal res
    #         if len(subset) == n:
    #             res.append(subset[:])
    #             return
            
    #         for j in range(len(nums)):
    #             if nums[j] not in subset:
    #                 subset.append(nums[j])
    #                 backtrack(subset)
    #                 subset.pop()
        
    #     backtrack([])
    #     return res