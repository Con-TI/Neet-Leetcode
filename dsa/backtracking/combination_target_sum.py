class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(i, subset):
            nonlocal res
            if sum(subset) == target:
                res.append(subset[:])

            for j in range(i, len(nums)):
                if sum(subset) + nums[j] <= target:
                    subset.append(nums[j])
                    backtrack(j, subset)
                    subset.pop()

        backtrack(0, [])
        return res