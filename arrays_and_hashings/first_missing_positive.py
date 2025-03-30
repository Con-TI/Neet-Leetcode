class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        smallestint = 1
        while smallestint in numSet:
            smallestint += 1
        return smallestint