class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Dynamic programming
        """
        # Idea: the memory/cache array is now a matrix to represent the 
        # substring window we consider. row num is the start index, 
        # col num is the length.
        # The dynamic programming part is simply checking the cache to see 
        # if the inner substring is a palindrome.
        resIdx, resLen = 0,0
        n = len(s)
        
        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i,n):
                # Check that ends match and 
                # that inner substring is also a palindrome
                if s[i]==s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if resLen < (j-i + 1):
                        resIdx = i
                        resLen = j - i + 1
        
        return s[resIdx : resIdx + resLen]
        """

        # Two ptr (O(n) memory instead of O(n^2))
        """
        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            # odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

            # even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1

        return s[resIdx : resIdx + resLen]
        """

        # Manacher's algorithm
        """
        def manacher(s):
            t = "#" + "#".join(s) + "#"
            n = len(t)
            p = [0] * n
            l,r = 0,0
            for i in range(n):
                p[i] = min(r - i, p[l + (r - i)]) if i < r else 0
                while (i + p[i] + 1 < n and i - p[i] - 1 >= 0
                       and t[i + p[i] + 1] == t[i - p[i] - 1]):
                    p[i] += 1
                if i + p[i] > r:
                    l, r = i - p[i], i + p[i]
            return p

        p = manacher(s)
        resLen, center_idx = max((v,i) for i,v in enumerate(p))
        resIdx = (center_idx - resLen) // 2
        return s[resIdx : resIdx + resLen]
        """
