class Solution:
    def numSquares(self, n: int) -> int:
        # Bottom up
        dp = [n] * (n+1)
        dp[0] = 0
        for target in range(1, n+1):
            for s in range(1, target + 1):
                square = s*s
                if target - square <0:
                    break
                dp[target] = min(dp[target], 1 + dp[target-square])
        return dp[n]

        # BFS
        q = deque()
        visit = set()
        res = 0
        q.append(0)
        while q:
            res += 1
            for _ in range(len(q)):
                cur = q.popleft()
                s = 1
                while s*s + cur <= n:
                    nxt = cur + s*s
                    if nxt == n:
                        return res
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append(nxt)
                    s += 1
        return res