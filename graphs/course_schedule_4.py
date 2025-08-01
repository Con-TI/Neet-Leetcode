class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Floyd Warshall Algorithm
        res = []
        adj = [[False] * numCourses for _ in range(numCourses)]

        for pre, crs in prerequisites:
            adj[pre][crs] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    adj[i][j] = adj[i][j] or (adj[i][k] and adj[k][j])

        for u,v in queries:
            res.append(adj[u][v])
        return res

        # Topo sort (Topo to generate the prereq then search)
        adj = [set() for _ in range(numCourses)]
        indegree = [0] * numCourses
        isPrereq = [set() for _ in range(numCourses)]

        for pre, crs in prerequisites:
            adj[pre].add(crs)
            indegree[crs] += 1
        
        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        while q:
            node = q.popleft()
            for nei in adj[node]:
                isPrereq[nei].add(node)
                isPrereq[nei].update(isPrereq[node])
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return [u in isPrereq[v] for u,v in queries]
        
        # Memoization (Generate a matrix to keep track of already verified prereqs for faster verification and search)
        adj = [[] for _ in range(numCourses)]
        isPrereq = [[-1]*numCourses for _ in range(numCourses)]
        for prereq, crs in prerequisites:
            adj[crs].append(prereq)
            isPrereq[crs][prereq] = True
        
        def dfs(crs, prereq):
            if isPrereq[crs][prereq] != -1:
                return isPrereq[crs][prereq] == 1

            for pre in adj[crs]:
                if pre == prereq or dfs(pre, prereq):
                    isPrereq[crs][prereq] = 1
                    return True
            
            isPrereq[crs][prereq] = 0
            return False
        
        res = []
        for u,v in queries:
            res.append(dfs(v,u))
        return res

        # Hash set (Find all prereqs and search)
        adj = defaultdict(list)
        for u,v in prerequisites:
            adj[v].append(u)
        
        def dfs(v):
            if v not in prereqMap:
                prereqMap[v] = set()
                for prereq in adj[v]:
                    prereqMap[v] |= dfs(prereq)
                prereqMap[v].add(v)
            return prereqMap[v]

        prereqMap = {}
        for v in range(numCourses):
            dfs(v)
        
        res = []
        for u,v in queries:
            res.append(u in prereqMap[v])
        return res

        # Brute force
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            adj[u].append(v)
        
        def dfs(node, target):
            if node == target:
                return True
            for nei in adj[node]:
                if dfs(nei, target):
                    return True
            return False

        res = []
        for u, v in queries:
            res.append(dfs(u, v))
        return res