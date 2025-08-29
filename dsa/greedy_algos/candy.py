class Solution:
    def candy(self, ratings):
        n = len(ratings)
        # At least 1 per child
        res = n
        i = 1
        while i < n:
            # Skip equal ratings
            if ratings[i] == ratings[i - 1]:
                i += 1
                continue

            # Increasing part
            # Every child gets more than the prior
            inc = 0
            while i < n and ratings[i] > ratings[i - 1]:
                inc += 1
                res += inc
                i += 1

            # Decreasing part
            # Every child gets less than the prior
            dec = 0
            while i < n and ratings[i] < ratings[i - 1]:
                dec += 1
                res += dec
                i += 1

            # If a decreasing and increasing part are next to each other
            # we delete the double counted section
            # which would be the overlapping child
            res -= min(inc, dec)
        return res