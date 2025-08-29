class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Kadane's Algo 
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0
        for num in nums:
            # Running maximum (regular Kadane)
            curMax = max(curMax + num, num)
            # Running minimum (modified Kadane)
            curMin = min(curMin + num, num)
            # Best max so far
            globMax = max(globMax, curMax)
            # Best min so far
            globMin = min(globMin, curMin)
            total += num

        # globMax considers the best subarray without looping around
        # total-globMin is the best subarray with looping
        # if globMax <= 0, then there are only 0 or negative nums, so total - globMin = 0
        # but we cannot return an empty array.
        return max(globMax, total-globMin) if globMax > 0 else globMax
        