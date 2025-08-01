class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        visited = set()
        
        def dfs(coords):
            i,j = coords
            if 0 <= i < m and 0 <= j < n and (i,j) not in visited and grid[i][j] == 1:
                visited.add((i,j))
                return 1 + dfs((i+1,j)) + dfs((i-1,j)) + dfs((i,j+1)) + dfs((i,j-1))
            return 0
            
        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i,j) not in visited:
                    max_area = max(max_area,dfs((i,j)))
        return max_area
