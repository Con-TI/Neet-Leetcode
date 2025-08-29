class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 31
        while n:
            res += (2**i) * (n%2)
            n //= 2
            i -= 1
        return res
