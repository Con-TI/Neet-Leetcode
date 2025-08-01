# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # BFS
        if not root:
            return 0
        queue = deque([root])
        i = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            i+=1 
        return i

        # Recursive DFS
        # if not root: return 0
        # return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        
        # Iterative DFS
        # if not root: return 0
        # stack = [(root,1)]
        # res = 0
        # while stack:
        #     node,depth = stack.pop()
        #     if node:
        #         res = max(res, depth)
        #         stack.append([node.left,depth+1])
        #         stack.append([node.right,depth+1])
        # return res