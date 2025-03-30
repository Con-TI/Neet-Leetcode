class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        ans = [1]*len(nums)
        for i,n in enumerate(nums):
            if i == 0:
                prefix[i] = n
                continue
            prefix[i] = n*prefix[i-1]
        for i,n in enumerate(reversed(nums)):
            j = len(nums)-i-1
            if i == 0:
                postfix[j] = n
                continue
            postfix[j] = n*postfix[j+1]
        ans[0] = postfix[1]
        ans[-1] = prefix[-2]
        for i in range(1,len(nums)-1):
            ans[i] = postfix[i+1]*prefix[i-1]
        return ans