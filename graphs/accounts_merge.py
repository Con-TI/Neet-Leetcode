class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # DFS (Similar to number of connected components)
        # Number of acc ids
        n = len(accounts)

        # email to idx mapping
        emailIdx = {}
        # Unique emails
        emails = []
        # email to accountid
        emailToAcc = {}

        m = 0
        for accId, a in enumerate(accounts):
            for i in range(1, len(a)):
                email = a[i]
                if email in emailIdx:
                    continue
                emails.append(email)
                emailIdx[email] = m
                emailToAcc[m] = accId
                m += 1
            
        # Adjacency list of emails sharing the same account id
        adj = [[] for _ in range(m)]
        for a in accounts:
            for i in range(2,len(a)):
                id1 = emailIdx[a[i]]
                id2 = emailIdx[a[i-1]]
                adj[id1].append(id2)
                adj[id2].append(id1)

        # Dictionary to keep track of similar account ids
        emailGroup = defaultdict(list)
        visited = [False]*m
        def dfs(node, accId):
            visited[node] = True
            emailGroup[accId].append(emails[node])
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei, accId)
            
        for i in range(m):
            if not visited[i]:
                dfs(i, emailToAcc[i])
            
        res = []
        for accId in emailGroup:
            name = accounts[accId][0]
            res.append([name] + sorted(emailGroup[accId]))
        
        return res