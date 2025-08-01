class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Negative marking (Marks the index using negative nums)
        # for num in nums:
        #     idx = abs(num) - 1
        #     if nums[idx] < 0:
        #         return abs(num)
        #     nums[idx] *= -1
        # return -1

        # Slow fast ptrs
        slow, fast = 0,0
        ## Cycle detection by meeting point (tortoise hare algo)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        ## Finding start point of the cycle
        ## (start to cycle start = int*cycle time - cycle start to meeting point )
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow