class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Iterations
        m, n, res = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += (i + 1 >= m or grid[i + 1][j] == 0)
                    res += (j + 1 >= n or grid[i][j + 1] == 0)
                    res += (i - 1 < 0 or grid[i - 1][j] == 0)
                    res += (j - 1 < 0 or grid[i][j - 1] == 0)
        return res

        # BFS
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))
            perimeter = 0
            
            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (nx < 0 or ny < 0 or nx >= rows or 
                        ny >= cols or grid[nx][ny] == 0
                    ):
                        perimeter += 1
                    elif (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            return perimeter
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return bfs(i, j)
        return 0

        # DFS
        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def dfs(i,j):
            if i<0 or j<0 or i>=rows or j >= cols or grid[i][j] == 0:
                return 1
            if (i,j) in visit:
                return 0

            visit.add((i,j))
            perim = dfs(i,j+1) + dfs(i+1,j) + dfs(i,j-1) + dfs(i-1,j)
            return perim
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(i,j)
        
        return 0