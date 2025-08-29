class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        # Build a list of edges
        edges = defaultdict(set)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    num1 = nums[i]
                    num2 = nums[j]
                    if self.calculateGcd(num1,num2) > 1:
                        edges[num1].add(num2)
                        edges[num2].add(num1)

        if not edges:
            return False

        # Do a bfs from any node. 
        # If one is not visited return False
        # Otherwise return true.
        start = list(edges.keys())[0]
        visit = set()
        q = deque([start])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node in visit:
                    continue
                visit.add(node)
                for node2 in edges[node]:
                    if node2 not in visit:
                        q.append(node2)
        
        return len(visit) == len(set(nums))

    def calculateGcd(self, num1, num2):
        # Euclidean algorithm
        if num1 == 0:
            return num2
        return self.calculateGcd(num2 % num1, num1)