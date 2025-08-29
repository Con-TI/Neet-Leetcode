class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Hash map
        # O(n^2) time
        # O(n) space
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num]+=1
        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1

            # Condition for i > 0
            # No duplicates
            if i and nums[i] == nums[i-1]:
                continue

            # Second pointer loop
            for j in range(i+1, len(nums)):
                count[nums[j]] -= 1

                # No duplicates
                if j-1 > i and nums[j] == nums[j-1]:
                    continue
                
                # Check the remaining number
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i],nums[j],target])

            for j in range(i+1, len(nums)):
                count[nums[j]] += 1
        return res