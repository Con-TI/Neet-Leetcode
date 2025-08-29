# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # DFS
        # def dfs(root):
        #     if not root:
        #         return [0,0]
            
        #     leftPair = dfs(root.left) # With root and without root vals
        #     rightPair = dfs(root.right) # With root and without root vals

        #     withRoot = root.val + leftPair[1] + rightPair[1] # Take without root vals
        #     withoutRoot = max(leftPair) + max(rightPair)

        #     return [withRoot, withoutRoot]
        
        # return max(dfs(root))

        # DFS with memoization
        cache = {None: 0}
        def dfs(root):
            if root in cache:
                return cache[root]
            
            cache[root] = root.val
            if root.left:
                cache[root] += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                cache[root] += dfs(root.right.left) + dfs(root.right.right)
            
            cache[root] = max(cache[root], dfs(root.left) + dfs(root.right))

            return cache[root]

        return dfs(root)