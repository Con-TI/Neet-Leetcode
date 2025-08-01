class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Hash map
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp and i-mp[nums[i]] <= k:
                return True
            mp[nums[i]] = i
        return False

        # Hash set
        window = set()
        L = 0
        for R in range(len(nums)):
            if R-L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False