class DSU:
    def __init__(self, n):
        self.Parent = list(range(n+1))
        self.Size = [1] * (n+1)

    def find(self,node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        # if pu == pv:
        #     return False
        if self.Size[pu] < self.Size[pv]:
            pu, pv = pv, pu
        self.Size[pu] += self.Size[pv]
        self.Parent[pv] = pu
        # return False

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Dijkstra's 
        # Kind of like BFS
        """
        ROWS, COLS = len(heights), len(heights[0])
        minHeap = [[0,0,0]] # diff, row, col
        visit = set()
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            
            if (r,c) in visit:
                continue
            
            visit.add((r,c))

            # Reached the end
            if (r,c) == (ROWS - 1, COLS - 1):
                return diff

            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if (
                    newR < 0 or newC < 0 or
                    newR >= ROWS or newC >= COLS or
                    (newR, newC) in visit
                ):
                    continue
            
                # Maximal difference between consecutive heights rule
                newDiff = max(diff, abs(heights[r][c] - heights[newR][newC]))
                heapq.heappush(minHeap, [newDiff, newR, newC])

        return 0"""

        # Kruskal's algorithm
        # i,j are numbered linearly: i*rows + j
        # edges are made between every single adjacent cell
        ROWS, COLS = len(heights), len(heights[0])
        edges = []
        for r in range(ROWS):
            for c in range(COLS):
                if r + 1 < ROWS:
                    edges.append((abs(heights[r][c] - heights[r + 1][c]), r * COLS + c, (r + 1) * COLS + c))
                if c + 1 < COLS:
                    edges.append((abs(heights[r][c] - heights[r][c + 1]), r * COLS + c, r * COLS + c + 1))

        # Sort the edges by smallest weights first
        edges.sort()
        # DSU with rows*cols nodes for every cell
        dsu = DSU(ROWS * COLS)


        for weight, u, v in edges:
            dsu.union(u, v)
            # The first time the nodes connect, it is the minimal abs max diff
            # since we've already sorted the edges before hand
            # so connecting the lowest weight ones till we find our first connection
            # will let us find the appropriate path.
            if dsu.find(0) == dsu.find(ROWS * COLS - 1):
                return weight
        
        return 0