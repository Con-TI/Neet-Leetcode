class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Ptrs
        # O(n) time
        # O(1) space
        i = j = 0
        while i<len(nums):
            nums[j] = nums[i]
            while i<len(nums) and nums[i]==nums[j]:
                i+=1
            j+=1
        return j

        # Sorted set
        # O(nlogn) time
        # O(n) space
        unique = sorted(set(nums))
        nums[:len(unique)] = unique
        return len(unique)