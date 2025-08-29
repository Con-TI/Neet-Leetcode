class Solution:
    def mySqrt(self, x: int) -> int:
        # Binary search
        l, r = 0,x
        res = 0
        while l<=r:
            m = l+(r-l)//2
            if m*m > x:
                r = m-1
            elif m*m < x:
                l = m+1
                res = m
            else:
                return m
        return res

        # Newton's method (Find the zero of r^2-x by shifting r)
        r = x
        while r*r > x:
            r = (r+x//r) // 2
        return r

        # While loop
        guess = 0
        while (guess+1)*(guess+1) <= x:
            guess += 1
        return guess