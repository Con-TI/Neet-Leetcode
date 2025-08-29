class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # In order traversal (Build array of ordered values)
        arr = []
        def dfs(node):
            if not node:
                return
        
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return arr[k-1]

        # Morris traversal (O(1) extra space)
        # curr = root
        # while curr:
        #     if not curr.left:
        #         k -= 1
        #         if k == 0:
        #             return curr.val
        #         curr = curr.right
        #     else:
        #         pred = curr.left
        #         while pred.right and pred.right != curr:
        #             pred = pred.right
                
        #         if not pred.right:
        #             pred.right = curr
        #             curr = curr.left
        #         else:
        #             pred.right = None
        #             k -= 1
        #             if k == 0:
        #                 return curr.val
        #             curr = curr.right
        
        # return -1