class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, subset):
            nonlocal res
            # Appends a reference instead of a new list
            # if we do res.append(subset). So we add [:] to generate
            res.append(subset[:])

            for j in range(i, len(nums)):
                subset.append(nums[j])
                # Re-run backtrack (using j+1 prevents double counting)
                backtrack(j+1, subset)
                subset.pop()
        
        backtrack(0,[])
        return res