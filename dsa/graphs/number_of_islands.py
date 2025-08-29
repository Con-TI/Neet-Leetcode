class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        visited = set()
        def dfs(coords):
            i, j = coords
            if  0 <= i < m and 0 <= j < n and grid[i][j] == "1" and (i,j) not in visited:
                visited.add((i,j))
                dfs((i+1,j))
                dfs((i-1,j))
                dfs((i,j+1))
                dfs((i,j-1))

        nums = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs((i,j))
                    nums += 1

        return nums