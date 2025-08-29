class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, v1):
        while v1 != self.par[v1]:
            self.par[v1] = self.par[self.par[v1]]
            v1 = self.par[v1]
        return v1

    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Kruskal's
        """
        # Make edges a list of (v1, v2, weight, original idx)
        for i,e in enumerate(edges):
            e.append(i)

        # Sort by lowest weight
        edges.sort(key=lambda e: e[2])


        # Construct an mst
        mst_weight = 0
        uf = UnionFind(n)
        for v1,v2, w, i in edges:
            if uf.union(v1,v2):
                mst_weight += w


        # Find the critical and pseudo edges
        critical, pseudo = [], []
        for n1, n2, e_weight, i in edges:
            # Try the mst without the current edge
            weight = 0
            uf = UnionFind(n)
            for v1, v2, w, j  in edges:
                if i != j and uf.union(v1,v2):
                    weight += w
            
            # If the weight increases with removal,
            # or the mst can't be completed (max rank != number of nodes)
            # add to the critical list
            if max(uf.rank) !=n or weight > mst_weight:
                critical.append(i)
                continue

            uf = UnionFind(n)
            uf.union(n1,n2)
            weight = e_weight
            for v1,v2, w, j in edges:
                if uf.union(v1,v2):
                    weight += w
            # Non critical but can form an mst implies edge is pseudo
            if weight == mst_weight:
                pseudo.append(i)
        
        return [critical,pseudo]
        """
        # Dijkstra's
        for i,edge in enumerate(edges):
            edge.append(i)

        adj = defaultdict(list)
        for u,v,w, idx in edges:
            adj[u].append((v,w,idx))
            adj[v].append((u,w,idx))
        
        def minimax(src, dst, exclude_idx):
            # Finds the minimum of the max edge weight
            # on any path from src to dst 
            dist = [float('inf')] * n
            dist[src] = 0
            pq = [(0,src)]

            while pq:
                max_w, u = heapq.heappop(pq)
                if u == dst:
                    return max_w
                for v, weight, edge_idx in adj[u]:
                    if edge_idx == exclude_idx:
                        continue
                    new_w = max(max_w, weight)
                    if new_w < dist[v]:
                        dist[v] = new_w
                        heapq.heappush(pq, (new_w,v))

            return float('inf')

        critical, pseudo = [], []
        for i, (u,v,w,idx) in enumerate(edges):
            # Exclude index specified
            # The edge i is the only way to connect 
            # the mst with said low weight, making it critical
            if w < minimax(u,v,idx):
                critical.append(idx)
            # The edge can be included in some MSTs but not necessary
            elif w == minimax(u,v,-1):
                pseudo.append(idx)

        return [critical, pseudo]