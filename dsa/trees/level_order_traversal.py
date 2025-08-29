# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BST
        if not root:
            return []

        res = []
        queue = deque([root])
        while queue:
            layer = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    layer.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if layer:
                res.append(layer)
        
        return res
