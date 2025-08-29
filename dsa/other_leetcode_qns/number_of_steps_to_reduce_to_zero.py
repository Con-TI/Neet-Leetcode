class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        k = 0
        while num:
            if num%2 == 1:
                num -= 1
            else:
                num //= 2
            k += 1
        return k