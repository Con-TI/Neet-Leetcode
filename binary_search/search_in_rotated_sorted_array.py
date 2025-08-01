class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # One pass binary search
        l = 0
        r = len(nums)-1 
        while l<=r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            if nums[l]<=nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return -1

        # Pivot based (Two pass binary search)
        l = 0
        r = len(nums)-1
        min_num = nums[r]
        min_idx = r

        while l<=r:
            m = (l+r)//2
            if nums[m] < min_num:
                min_num = nums[m]
                min_idx = m
                r = m-1
            elif nums[m] > min_num:
                l = m+1
            else:
                break

        pivot = min_idx

        l = 0
        r = len(nums) - 1

        while l<=r:
            m = ((l+r)//2 + pivot) % len(nums)
            if nums[m] < target:
                l = (l+r)//2 + 1
            elif nums[m] > target:
                r = (l+r)//2 - 1
            else:
                return m
        
        return -1

