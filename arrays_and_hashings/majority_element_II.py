class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) <= 2:
            return list(set(nums))
        
        lower_bound_count = len(nums)//3
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        res = []
        for key in counts:
            if counts[key]>lower_bound_count:
                res.append(key)
        return res
