# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, root: Optional[TreeNode], subRoot:Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            # Proceeds to check further
            return (self.sameTree(root.left, subRoot.left) and 
                   self.sameTree(root.right, subRoot.right))
        return False

    def serialize(self, root):
        # Converts into a coded string
        if root == None:
            return "$#"
        return ("$" + str(root.val) + self.serialize(root.left) + self.serialize(root.right))
    
    def z_function(self, s):
        # z-algorithm which creates an array z of length same with s such that
        # z[i] stores the length of the longest substring starting from s[i]
        # that is also a prefix of s
        z = [0] * len(s)
        l, r, n = 0, 0, len(s)
        for i in range(1,n):
            if i<=r:
                z[i] = min(r-i+1, z[i-1])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] -1
        return z

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #DFS
        # if not subRoot:
        #     return True
        # if not root:
        #     return False

        # if self.sameTree(root, subRoot):
        #     return True
        # return (self.isSubtree(root.left, subRoot) or 
        #        self.isSubtree(root.right, subRoot))

        # Serialization and pattern matching 
        # (converts roots to strings and matches using z array
        # since the array is unique and subRoot is serialized at the start)
        serialized_root = self.serialize(root)

        serialized_subRoot = self.serialize(subRoot)
        combined = serialized_subRoot + "|" + serialized_root
        z_values = self.z_function(combined)
        sub_len = len(serialized_subRoot)
    
        for i in range(sub_len + 1, len(combined)):
            if z_values[i] == sub_len:
                return True
        return False