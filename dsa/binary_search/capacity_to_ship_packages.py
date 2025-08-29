class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        while l<=r:
            m = (l+r)//2
            
            totalTime = 0 
            curweight = 0 
            for weight in weights:
                curweight += weight
                if curweight>m:
                    totalTime += 1
                    curweight = weight
            totalTime += 1

            if totalTime > days:
                l = m+1
            elif totalTime <= days:
                res = min(res,m)
                r = m-1

        return res