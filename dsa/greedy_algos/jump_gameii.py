class Solution:
    def jump(self, nums: List[int]) -> int:
        # Idea: Explore a larger and larger range until it includes the end
        res = 0
        l = 0
        r = 0
        # Kind of BFS
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            l = r + 1
            r = farthest
            res += 1
        
        return res
