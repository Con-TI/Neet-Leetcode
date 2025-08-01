def binary(l,r,nums,target):
        if l>r:
            return l
        else:
            m = l+(r-l)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                return binary(m+1,r,nums,target)
            elif nums[m] > target:            
                return binary(l,m-1,nums,target)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return binary(0,len(nums)-1,nums,target)