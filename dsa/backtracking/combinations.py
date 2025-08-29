class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1,n+1))
        res = []
        def backtrack(i, subset):
            if len(subset) == k:
                res.append(subset[:])
            
            for j in range(i, len(nums)):
                subset.append(nums[j])
                backtrack(j+1, subset)
                subset.pop()
            
        backtrack(0,[])

        return res