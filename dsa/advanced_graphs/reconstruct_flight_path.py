class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # DFS
        """
        edges = {src:[] for src, dst in tickets}

        tickets.sort()
        for src, dst in tickets:
            edges[src].append(dst)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True

            if src not in edges:
                return False
            
            temp = list(edges[src])
            for i,v in enumerate(temp):
                # Backtracking
                edges[src].pop(i)
                res.append(v)
                if dfs(v): 
                    return True
                edges[src].insert(i,v)
                res.pop()

        dfs("JFK")
        return res
        """
        # Hierholzer's algo (Post order traversal)
        edges = defaultdict(list)
        for src,dst in sorted(tickets)[::-1]:
            edges[src].append(dst)
        
        res = []
        def dfs(src):
            while edges[src]:
                dst = edges[src].pop()
                dfs(dst)
            res.append(src)

        dfs("JFK")
        return res[::-1]
