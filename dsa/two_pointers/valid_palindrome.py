class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ord("a")
        ref = ""
        s = s.lower()
        for c in s:
            if c.isalpha() or c.isnumeric():
                ref += c
        if len(ref) <= 1:
            return True
        half = len(s)//2
        j = -1
        for i in range(half+1):
            if ref[i] != ref[j]:
                return False
            j -= 1
        return True