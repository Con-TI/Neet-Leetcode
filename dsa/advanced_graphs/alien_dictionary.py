class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # TOPOSORT
        # Assumed to point towards the higher order alphabet letter
        adj = {c:set() for w in words for c in w}
        indegree = {c:0 for c in adj}

        # Build up adjacency and indegree list
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1),len(w2))
            # Invalid order based on lexiographic ordering
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        

        q = deque([c for c in indegree if indegree[c] == 0])
        res = []

        while q:
            char = q.popleft()
            res.append(char)
            for nei in adj[char]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        if len(res) != len(indegree):
            return ""

        return "".join(res)

        

