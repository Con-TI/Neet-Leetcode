class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] means: does s[i:] match p[j:]
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Empty pattern matches empty string
        dp[len(s)][len(p)] = True

        # Traverse dp table from the bottom up
        # i points to position in s
        for i in range(len(s), -1, -1):
            # j points to position in p
            for j in range(len(p) - 1, -1, -1):

                # Check if characters match at s[i] and p[j], or if p[j] is '.'
                # Only valid if i is still within bounds of s
                condition = i < len(s) and (s[i] == p[j] or p[j] == '.')

                # Case when the next character in pattern is '*'
                if (j + 1) < len(p) and p[j + 1] == "*":
                    # Two choices:
                    # 1. Skip the current character and the '*', i.e., treat as zero occurrence
                    # 2. If condition is true, consume one character from s and stay on p[j]
                    dp[i][j] = dp[i][j + 2] or (condition and dp[i + 1][j])
                
                # No '*' wildcard following
                elif condition:
                    # Proceed to check the rest: s[i+1:] with p[j+1:]
                    dp[i][j] = dp[i + 1][j + 1]
        
        # Final answer: does the entire s match the entire p?
        return dp[0][0]
