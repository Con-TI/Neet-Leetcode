# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # DFS
        # res = []

        # def postorder(node):
        #     if not node:
        #         return

        #     postorder(node.left)
        #     postorder(node.right)            
        #     res.append(node.val)

        # postorder(root)
        # return res

        # Iterative DFS 1
        # stack = [root]
        # visit = [False]
        # res = []
        # while stack:
        #     cur, v = stack.pop(), visit.pop()
        #     if cur:
        #         if v:
        #             res.append(cur.val)
        #         else:
        #             stack.append(cur)
        #             visit.append(True)
        #             stack.append(cur.right)
        #             visit.append(False)
        #             stack.append(cur.left)
        #             visit.append(False)

        # return res

        # Iterative DFS 2
        # res = []
        # stack = []
        # cur = root
        # while cur or stack:
        #     if cur:
        #         res.append(cur.val)
        #         stack.append(cur)
        #         cur = cur.right
        #     else:
        #         cur = stack.pop()
        #         cur = cur.left
        
        # res.reverse()
        # return res

        # Morris Traversal (fill based on root right left traversal then reverse. 
        # same as preorder just with reverse at the end)
        res = []
        cur = root

        while cur:
            if not cur.right:
                res.append(cur.val)
                cur = cur.left
            else:
                prev = cur.right
                while prev.left and prev.left != cur:
                    prev = prev.left

                if not prev.left:
                    res.append(cur.val)
                    prev.left = cur
                    cur = cur.right
                else:
                    prev.left = None
                    cur = cur.left
                    
        res.reverse()
        return res