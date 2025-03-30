class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 2:
            return True

        
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return (is_palindrome(l + 1, r) or 
                        is_palindrome(l, r - 1))
            l += 1
            r -= 1

        return True