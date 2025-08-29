class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Works recursively.
        # Loops through all 3 sums which are each a loop of possible 2 sums.
        nums.sort()
        res, quad = [], []

        # Function to find k sum
        def kSum(k, start, target):
            if k == 2:
                l,r = start, len(nums)-1
                while l<r:
                    if nums[l] + nums[r] < target:
                        l+=1
                    elif nums[l] + nums[r] > target:
                        r -= 1
                    else:
                        # If we reach the target, add to list
                        res.append(quad+[nums[l],nums[r]])
                        # Shift
                        l+=1
                        r-=1
                        # Get to the next index where it isn't just a repeat
                        while l<r and nums[l] == nums[l-1]:
                            l += 1
                        while l<r and nums[r] == nums[r+1]:
                            r -= 1
                        # Go through the loop again to check for 
                        # target matches with different indices.
                return

            for i in range(start, len(nums)-k+1):
                # check for repeats/duplicates if i>start                
                if i>start and nums[i] == nums[i-1]:
                    continue
                # quad always has 2 elements in it from 4 and 3 sum.
                quad.append(nums[i])
                kSum(k-1, i+1, target-nums[i])
                quad.pop()
        
        kSum(4,0,target)
        return res