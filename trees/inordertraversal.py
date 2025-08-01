# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
In-order traversal refers to left-root-right traversal
"""

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # DFS O(n) memory from recursion
        res = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        inorder(root)
        return res

        # Iterative DFS O(n) memory from stack (Just like the recursion version)
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res

        # Morris Traversal O(1) extra space, uses prev pointer to go back
        res = []
        cur = root
        while cur:
            if not cur.left:
                res.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right!=cur:
                    prev = prev.right

                # prev node has no right pointer
                if not prev.right:
                    prev.right = cur
                    cur = cur.left
                # prev node has a right pointer
                else:
                    prev.right = None
                    res.append(cur.val)
                    cur = cur.right

