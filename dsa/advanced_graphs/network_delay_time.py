class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's 
        """
        # Not like BFS in that it does one node at a time instead of in groups
        # Operates depending on some running size/value/metric
        edges = defaultdict(list) # list of edges with edge weights
        for u, v, w in times:
            edges[u].append([v,w])

        minHeap = [(0,k)]
        visit = set()
        t = 0
        while minHeap:
            # weight, node
            # Tries minimal total running weight paths
            w1, n1 = heapq.heappop(minHeap)

            if n1 in visit:
                continue
            visit.add(n1)
            t = w1
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        return t if len(visit) == n else -1
        """
        # Shortest path faster
        """# Better than bellman ford, only visits an edge when it has potential
        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))

        # Distance of each node
        dist = {node : float('inf') for node in range(1, n+1)}
        q = deque([[k,0]])
        dist[k] = 0

        while q:
            node, time = q.popleft()
            # Ignore if the time is too long
            if dist[node] < time:
                continue

            for nei, w in adj[node]:
                # Explore if the path to nei is shorter than what exists
                if time + w < dist[nei]:
                    # Update with better distance
                    dist[nei] = time + w
                    q.append((nei, time + w))

        # If there is an infinity, that means there was no visit to said node
        res = max(dist.values())
        return res if res < float('inf') else -1
        """
        
        # Bellman ford algorithm
        """
        dist = [float('inf')] * n
        dist[k-1] = 0
        for _ in range(n-1):
            for u, v, w in times:
                if dist[u-1] + w < dist[v-1]:
                    dist[v-1] = dist[u-1] + w
        max_dist = max(dist)
        return max_dist if max_dist < float('inf') else -1
        """

        # Floyd Warshall
        # Works by starting with the edges as the distances
        # Then trying out every single possible a -> b -> c combination.
        inf = float('inf')
        dist = [[inf] * n for _ in range(n)]

        for u,v,w in times:
            dist[u-1][v-1] = w
        
        for i in range(n):
            dist[i][i] = 0 
        
        for mid in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][mid] + dist[mid][j])
        
        res = max(dist[k-1])
        return res if res < inf else -1


        # DFS
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        dist = {node: float("inf") for node in range(1, n + 1)}

        def dfs(node, time):
            if time >= dist[node]:
                return
            
            dist[node] = time
            for nei, w in adj[node]:
                dfs(nei, time + w)
        
        dfs(k, 0)
        res = max(dist.values())
        return res if res < float('inf') else -1