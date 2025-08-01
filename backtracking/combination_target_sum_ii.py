class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # Ensures same nums are next to each other
        candidates.sort()

        def backtrack(i, path):
            # Include if it matches
            if sum(path) == target:
                res.append(path[:])
                return
            
            for j in range(i, len(candidates)):
                # Skip repeats 
                # This avoids issues with candidates like [1,2,2,5]
                # that would otherwise double count since it sees the two 2s as unique.
                # i.e. we'd output [1,2,5] twice.
                if j>i and candidates[j] == candidates[j-1]:
                    continue

                # All subsequent candidates would be higher so can skip exploring
                if sum(path) + candidates[j] > target:
                    break
                

                path.append(candidates[j])
                backtrack(j+1, path)
                path.pop()

        backtrack(0,[])
        return res