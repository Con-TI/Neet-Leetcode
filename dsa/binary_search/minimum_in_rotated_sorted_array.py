class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_num = nums[-1]

        while l<=r:
            m = (l+r)//2
            if nums[m] < min_num:
                r = m-1
                min_num = nums[m]
            elif nums[m] > min_num:
                l = m+1
            else:
                break

        return min_num
                