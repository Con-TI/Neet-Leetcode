class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        # Idea: Assign the importances based on the degree of each node

        degree = [0 for _ in range(n)]

        for a,b in roads:
            degree[a] += 1
            degree[b] += 1
        
        degree.sort()

        res = 0
        for i in range(1,n+1):
            res += i*degree[i-1]
        return res
