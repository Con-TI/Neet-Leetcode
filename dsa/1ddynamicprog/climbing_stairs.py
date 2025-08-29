class Solution:
    def climbStairs(self, n: int) -> int:
        # Top down DP
        """
        dp = [-1] * n
        def dfs(i):
            if i >= n:
                return i == n
            if dp[i] != -1:
                return dp[i]
            # Number of ways starting from i
            # is equal to the number of ways from i+1 (take 1 step)
            # + number of ways from i+2 (take 2 step)
            dp[i] = dfs(i+1) + dfs(i+2)
            return dp[i]
        return dfs(0)
        """

        # Bottom up DP
        # if n <= 2:
        #     return n
        # dp = [0] * (n+1)
        # dp[1], dp[2] = 1,2
        # for i in range(3, n+1):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n]

        # DP Constant space
        """
        one, two = 1,1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
        """

        # Matrix exponentiation
        """
        if n==1:
            return 1
        def matrix_mult(A,B):
            return [[sum([A[i][k]*B[k][j]for k in range(len(A[0]))]) for i in range(len(A))] for j in range(len(B))]

        def matrix_pow(M,p):
            result = [[1,0],[0,1]]
            base = M
            while p:
                if p%2 == 1:
                    result = matrix_mult(result, base)
                base = matrix_mult(base,base)
                p //= 2
            return result

        M = [[1,1],[1,0]]
        result = matrix_pow(M,n)
        return result[0][0]
        """