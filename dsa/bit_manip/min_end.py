class Solution:
    def minEnd(self, n: int, x: int) -> int:

        res = x
        i_x = 1
        i_n = 1
        while i_n <= n - 1:
            # If the bit in x is 0
            if i_x & x == 0:
                # We check if (i_n)th bit is 1 in n-1
                if i_n & (n-1):
                    # If it is then flip it to 1
                    # Otherwise skip
                    res = res | i_x
                # Increment the n
                i_n = i_n << 1
            # Increment the x always
            i_x = i_x << 1

        return res