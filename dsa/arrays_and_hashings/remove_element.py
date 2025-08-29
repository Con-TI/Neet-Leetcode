class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0 
        for i, n in enumerate(nums):
            if n != val:
                nums[k] = nums[i]
                k += 1
        return k

        n = len(nums)
        k = 0
        while val in nums:
            nums.remove(val)
            k += 1
        return n-k