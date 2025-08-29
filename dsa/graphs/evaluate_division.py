class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Main idea: You can construct a mapping like exchange rates
        Then if it is possible to calculate with the given info you'd
        be able to traverse the mapping/graph until A1, A2,..,Ak to get A1/Ak
        multiplying the factor each time
        """


        graph = {}
        for i,eq in enumerate(equations):
            ai, bi = eq
            if ai not in graph:
                graph[ai] = []
            if bi not in graph:
                graph[bi] = []
            graph[ai].append((bi, values[i]))
            graph[bi].append((ai, 1.0/values[i]))

        res = []
        for query in queries:
            flag = False
            ai, bi = query

            if ai not in graph:
                res.append(-1.0)
                continue

            if ai == bi:
                res.append(1.0)
                continue

            # BFS
            visit = set()
            queue = deque([(ai,1.0)])
            while queue:
                for _ in range(len(queue)):
                    node, running_val = queue.popleft()
                    visit.add(node)
                    if node not in graph:
                        continue
                    for nei in graph[node]:
                        if nei[0] not in visit:
                            if nei[0] == bi:
                                flag = True
                                res.append(running_val*nei[1])
                                break
                            queue.append((nei[0], running_val * nei[1]))
                    if flag:
                        break
                if flag:
                    break

            if not flag:
                res.append(-1.0)

        return res