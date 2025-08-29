class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])
        
        directions = [(1,0),(-1,0), (0,1), (0,-1)]
        
        minHeap = [(grid[0][0], 0,0)] # (total_cost, node)
        visit = set()

        while minHeap:
            total_cost, i,j = heapq.heappop(minHeap)
            visit.add((i,j))
            if i == ROWS-1 and j == COLS-1:
                return total_cost

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (ni < 0 or ni >= ROWS 
                or nj < 0 or nj >= COLS
                or (ni,nj) in visit):
                    continue

                heapq.heappush(minHeap, (max(total_cost,grid[ni][nj]),ni, nj))