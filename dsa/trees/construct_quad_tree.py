"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # Recursion O(n^2 log n) time, O(logn) space
        # def dfs(n, r, c):
        #     allSame = True
        #     for i in range(n):
        #         for j in range(n):
        #             if grid[r][c] != grid[r + i][c + j]:
        #                 allSame = False
        #                 break
        #     if allSame:
        #         return Node(grid[r][c], True)
        
        #     n = n//2
        #     topleft = dfs(n,r,c)
        #     topright = dfs(n,r,c + n)
        #     bottomleft = dfs(n, r + n, c)
        #     bottomright = dfs(n, r + n, c + n)

        #     return Node(0, False , topleft, topright, bottomleft, bottomright)
        # return dfs(len(grid), 0, 0)

        # Recursion Optimal O(n^2) time, O(logn) space 
        # def dfs(n, r, c):
        #     # Minimal block
        #     if n == 1:
        #         return Node(grid[r][c] == 1, True)
        #     mid = n//2
        #     topLeft = dfs(mid, r, c)
        #     topRight = dfs(mid, r, c + mid)
        #     bottomLeft = dfs(mid, r + mid, c)
        #     bottomRight = dfs(mid, r + mid, c + mid)

        #     # Combine if they are all one block (no splits, all dirs point to null)
        #     if (topLeft.isLeaf and topRight.isLeaf and 
        #     bottomLeft.isLeaf and bottomRight.isLeaf and
        #     topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
        #         return Node(topLeft.val, True)

        #     # Return a node that splits into 4
        #     return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)

        # return dfs(len(grid), 0, 0) 

        # Recursion Space Optimized
        leafNodes = {
            0 : Node(False, True),
            1 : Node(True, True)
        }

        def dfs(n, r, c):
            if n == 1:
                return leafNodes[grid[r][c]]
            
            n //= 2
            topLeft = dfs(n, r, c)
            topRight = dfs(n, r, c + n)
            bottomLeft = dfs(n, r + n, c)
            bottomRight = dfs(n, r + n, c + n)

            if (topLeft.isLeaf and topRight.isLeaf and 
                bottomLeft.isLeaf and bottomRight.isLeaf and
                topLeft.val == topRight.val == bottomLeft.val == bottomRight.val):
                return topLeft

            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)

        return dfs(len(grid), 0, 0)