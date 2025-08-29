class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 0
        n = len(str(num))
        while i < n:
            if (num // 10 ** (n-1-i)) % 10 == 6:
                return num + 3*(10 ** (n-1-i))
            i += 1
        return num
