class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Dynamic Programming (Recursively generating up to n pairs)
        res = [[] for _ in range(n+1)]
        res[0] = [""]

        for k in range(n + 1):
            for i in range(k):
                for left in res[i]:
                    for right in res[k-i-1]:
                        res[k].append("(" + left + ")" + right)
        
        return res[-1]

        # Backtracking
        stack = []
        res = []
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
        
            if openN<n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0)
        return res
