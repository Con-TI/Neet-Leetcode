# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # DFS
        res = []
        def preorder(node):
            if not node:
                return
            
            res.append(node.val)
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return res

        # Iterative DFS
        res = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                cur = cur.left
            else:
                cur = stack.pop()
            
        return res

        # Morris traversal (Similar to in order except append lines moved)
        res = []
        cur = root
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                
                if not prev.right:
                    res.append(cur.val)
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    cur = cur.right
        return res