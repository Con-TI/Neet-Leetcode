class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [i for i in range(n)]
        graph = {}

        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            if edge[1] not in graph:
                graph[edge[1]] = []            
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        height_to_root = {}
        min_height = float('inf')
        for node in graph.keys():
            # Perform BFS to figure out the height
            visit = set()
            q = deque([node])
            height = -1
            while q:
                height += 1
                for _ in range(len(q)):
                    cur = q.popleft()
                    visit.add(cur)
                    for nei in graph[cur]:
                        if nei not in visit:
                            q.append(nei)
            if height not in height_to_root:
                height_to_root[height] = []
            height_to_root[height].append(node)
            min_height = min(height, min_height)

        # Take the minimum list
        return height_to_root[min_height]