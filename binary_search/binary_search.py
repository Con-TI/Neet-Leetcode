class Solution:
    def binary(self,l,r,nums,target) -> int:
        if l>r:
            return -1
        m = l + (r-l) //2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            return self.binary(m+1,r,nums,target)
        elif nums[m] > target:
            return self.binary(l,m-1,nums,target)

    def search(self, nums: List[int], target: int) -> int:
        return self.binary(0,len(nums)-1,nums,target)