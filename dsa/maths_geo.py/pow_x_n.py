class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 0:
            return 1

        res = 1
        if n > 0:
            power = x
            while n:
                if n%2:
                    res *= power 
                power = power*power
                n //= 2
        elif n < 0:
            n = abs(n)
            power = 1/x
            while n:
                if n%2:
                    res *= power
                power = power*power
                n = abs(n) // 2
        return res
