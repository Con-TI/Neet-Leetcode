# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Iteration

        if not root:
            return root

        parent = None
        cur = root

        while cur and cur.val != key:
            parent = cur
            if key > cur.val:
                cur = cur.right
            else:
                cur = cur.left
        
        if not cur:
            return root

        if not cur.left or not cur.right:
            # One or no child
            child = cur.left if cur.left else cur.right
            if not parent:
                return child
            if parent.left == cur:
                parent.left = child
            else:
                parent.right = child
        else:
            # Two children
            par = None
            delNode = cur
            cur = cur.right
            while cur.left:
                par = cur
                cur = cur.left
            
            # If there was left traversal
            if par:
                par.left = cur.right
                cur.right = delNode.right
            
            cur.left = delNode.left

            if not parent:
                return cur
            
            if parent.left == delNode:
                parent.left = cur
            else:
                parent.right = cur

        return root