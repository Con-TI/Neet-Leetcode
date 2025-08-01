# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # DFS
        def dfs(node_p, node_q):
            if node_p is None or node_q is None:
                if node_p is None and node_q is None:
                    return True
                else:
                    return False

            if node_p.val != node_q.val:
                return False
            else:
                return dfs(node_p.left, node_q.left) and dfs(node_p.right, node_q.right)
            
        return dfs(p, q)

        # Iterative DFS

        # stack = [(p,q)]
        # while stack:
        #     node1, node2 = stack.pop()
        #     if not node1 and not node2:
        #         continue
        #     if not node1 or not node2 or node1.val != node2.val:
        #         return False
            
        #     stack.append((node1.right, node2.right))
        #     stack.append((node1.left, node2.left))
        
        # return True
        
        # BFS
        # q1 = deque([p])
        # q2 = deque([q])

        # while q1 and q1:
        #     for _ in range(len(q1)):
        #         nodeP = q1.popleft()
        #         nodeQ = q2.popleft()
        #         if nodeP is None and nodeQ is None:
        #             continue
        #         if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
        #             return False
        #         q1.append(nodeP.left)
        #         q1.append(nodeP.right)
        #         q2.append(nodeQ.left)
        #         q2.append(nodeQ.right)
        
        # return True