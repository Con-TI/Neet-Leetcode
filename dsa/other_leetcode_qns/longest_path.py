class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        # DFS
        children = [[] for i in range(len(s))]
        for i, j in enumerate(parent):
            # Parent of i is j
            if j >= 0:
                children[j].append(i)
        
        res = 0
        def dfs(i):
            nonlocal res
            candi = [0]
            for j in children[i]:
                # Look at the traversal through its children
                # This step also records the best paths from subtree j
                cur = dfs(j)
                if s[i] != s[j]:
                    candi.append(cur)

            # Two largest paths with subtree from node i
            # Best path including node i
            candi = nlargest(2, candi)

            # Running best result
            res = max(res, sum(candi) + 1)

            # Returns the best one sided path
            return max(candi) + 1
        
        dfs(0)
        return res