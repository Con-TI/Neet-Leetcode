class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        i = 1
        while self.check_zero(i) or self.check_zero(n-i):
            i += 1
        return [i, n-i]
        
    def check_zero(self, num):
        while num:
            if num % 10 == 0:
                return True
            num //= 10
        return False