class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Idea: A running negative can flip to a positive. 
        # So also include the negatives in the cache of the method of choice

        # Sliding window
        A = [] # List of subarrays (excluding 0s)
        cur = [] # Current subarray
        res = float('-inf')

        for num in nums:
            res = max(res, num)
            if num == 0:
                if cur:
                    A.append(cur)
                cur = []
            else:
                cur.append(num)
        if cur:
            A.append(cur)

        # For every sub array
        for sub in A:
            negs = sum(1 for i in sub if i < 0)
            prod = 1
            need = negs if negs % 2 == 0 else negs - 1 # Remove one negative to make prod positive if odd
            negs = 0 # Reset negs
            j = 0 # pointer

            for i in range(len(sub)):
                prod *= sub[i]
                # If a negative element and we have
                # too many negs, 
                # shrink the window from the left
                if sub[i] < 0:
                    negs += 1
                    while negs > need:
                        prod //= sub[j]
                        if sub[j] < 0:
                            negs -= 1
                        j += 1
                if j <= i:
                    res = max(res, prod)

        return res

        # Dynamic programming (Kadane's algorithm)
        res = nums[0]
        curMin, curMax = 1, 1

        for num in nums:
            tmp = curMax * num
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(res, curMax)
        return res

        # Prefix suffix
        n, res = len(nums), nums[0]
        prefix = suffix = 0
        for i in range(n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n-1-i] * (suffix or 1)
            res = max(res, max(prefix, suffix))
        return res