class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l,r = 0,len(arr)-1
        last_step = None
        while r-l+1>k:
            left = arr[l]
            right = arr[r]
            ldist = abs(left-x)
            rdist = abs(right-x)
            if ldist<=rdist:
                r-=1
            else:
                l+=1
        return arr[l:r] + [arr[r]]