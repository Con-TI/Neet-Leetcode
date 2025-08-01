class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # Backtracking (Same as combinations 2 algo)
        # nums.sort()
        # res = []
        # def backtrack(i, subset):
        #     res.append(subset[:])
        #     for j in range(i, len(nums)):
        #         if j > i and nums[j] == nums[j - 1]:
        #             continue

        #         subset.append(nums[j])
        #         backtrack(j + 1, subset)
        #         subset.pop()

        # backtrack(0, [])
        # return res

        # Iterations
        nums.sort()
        res = [[]] # Empty subset
        
        # prev_idx indicates length of the running set of subsets
        prev_idx = idx = 0
        for i in range(len(nums)):
            # Only explore/extend the new subsets added in the last iteration
            # If nums[i] is a duplicate of the prior num
            # Prevents exploring the same path as some prior run
            # E.g. nums = [2,2], we'd explore [2] twice if we didn't add the conditional
            if i>= 1 and nums[i] == nums[i-1]:
                idx = prev_idx
            else:
                idx = 0
            
            prev_idx = len(res)
        
            # Loops through valid subsets to explore
            for j in range(idx, prev_idx):
                tmp = res[j].copy()
                tmp.append(nums[i])
                res.append(tmp)
        
        return res