class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l<=r:
            m = l + (r-l)//2
            if nums[m] == target:
                return True
            
            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[l] > nums[m]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m-1
            else:
                # Either means l to m is a subarray of identical vals so we need to shift l
                # Or m to r is a subarray of identical vals, where we still need to shift l.
                # Shifting l allows us to work on a smaller relevant subarray.
                l += 1
        return False