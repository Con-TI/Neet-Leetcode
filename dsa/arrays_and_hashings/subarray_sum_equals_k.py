class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        total = 0
        
        prefix_map = defaultdict(int)
        prefix_map[0] += 1

        for i in range(1,len(nums)+1):
            s = sum(nums[:i])
            if prefix_map[s-k] > 0:
                total += prefix_map[s-k]
            prefix_map[s] += 1
        return total