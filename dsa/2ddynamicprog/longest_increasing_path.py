class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # We want to find the longest increasing path from every point in the grid
        # So we try DFS from every single point.
        # Then take the maximum among all these values

        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c, prevVal):
            # If out of bounds or does not satisfy path conditions
            if (r<0 or r==ROWS or c<0 or c==COLS or matrix[r][c] <= prevVal):
                return 0
            # If precomputed
            if (r,c) in dp:
                return dp[(r,c)]
            
            res = 1
            res = max(res,
                1 + dfs(r+1, c, matrix[r][c]),
                1 + dfs(r, c+1, matrix[r][c]),
                1 + dfs(r-1, c, matrix[r][c]),
                1 + dfs(r, c-1, matrix[r][c]))
            dp[(r,c)] = res
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())