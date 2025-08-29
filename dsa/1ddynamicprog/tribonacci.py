class Solution:
    def __init__(self):
        self.dp = {}
    def tribonacci(self, n: int) -> int:
        # Top down
        """
        if n <= 2:
            return 1 if n!= 0 else 0
        if n in self.dp:
            return self.dp[n]

        self.dp[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

        return self.dp[n]
        """

        # Bottom up
        """
        dp = [0] * max(3,n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[n]
        """

        # Space optimized
        if n <= 2:
            return 1 if n!= 0 else 0
        zero = 0
        one = 1
        two = 1
        for i in range(3,n+1):
            res = two + one + zero
            zero = one
            one = two
            two = res
        return two            