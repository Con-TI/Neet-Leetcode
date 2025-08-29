class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        hash_map = defaultdict(int)
        for n in nums:
            hash_map[n] += 1
        i = 0
        for key in hash_map:
            while hash_map[key] != 0:
                nums[i] = key
                hash_map[key] -= 1
                i += 1
        return nums

