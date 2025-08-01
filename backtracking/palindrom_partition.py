class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], [] # Results and running partition

        # Takes in a left ptr
        def dfs(i):
            # No more characters left
            if i >= len(s):
                res.append(part.copy())
                return
            
            # Iterate through every other character
            for j in range(i, len(s)):
                # Backtracking logic
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    # Look for more palindromes to add
                    dfs(j+1)
                    # Pop for backtrack
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True