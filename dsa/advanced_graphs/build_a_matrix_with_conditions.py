class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:        
        # Toposort
        # Idea: do toposort on rows to determine row indices
        # then do it on columns to determine column indices
    
        row_edges = defaultdict(list)
        row_indegree = {i+1:0 for i in range(k)}

        col_edges = defaultdict(list)
        col_indegree = {i+1:0 for i in range(k)}

        for above, below in rowConditions:
            row_edges[above].append(below)
            row_indegree[below] += 1

        for left, right in colConditions:
            col_edges[left].append(right)
            col_indegree[right] += 1

        # Perform toposort to find row indices
        q = deque([i for i in row_indegree if row_indegree[i] == 0])
        row_indices = {i:None for i in range(k)}
        visit = set()

        j = 0
        while q:
            node = q.popleft()
            if node in visit:
                continue
            visit.add(node)
            row_indices[node] = j
            j += 1
            for n2 in row_edges[node]:
                row_indegree[n2] -= 1
                if row_indegree[n2] == 0:
                    q.append(n2)

        if len(visit) != k:
            return []


        q = deque([i for i in col_indegree if col_indegree[i] == 0])
        col_indices = {i:None for i in range(k)}
        visit = set()

        j = 0
        while q:
            node = q.popleft()
            if node in visit:
                continue
            visit.add(node)
            col_indices[node] = j
            j += 1
            for n2 in col_edges[node]:
                col_indegree[n2] -= 1
                if col_indegree[n2] == 0:
                    q.append(n2)

        if len(visit) != k:
            return []

        matrix = [[0]*k for i in range(k)]
        for node in range(k):
            i = row_indices[node+1]
            j = col_indices[node+1]
            matrix[i][j] = node + 1
        
        return matrix