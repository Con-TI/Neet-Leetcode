class Solution(object):
    def maximumScore(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Problem: Strategically choose which cells to color black to maximize the
        # sum of white cells horizontally adjacent to black cells.

        # Idea: We try going column by column.
        # For dynamic programming requiring a future state (as in ours with the adjacency rule)
        # we can just calculate value for j-1 at iteration j.

        """
        # Plain brute force (all combis, ultimately too slow)
        n = len(grid)
        if n==1:
            return 0

        black_lengths = [0 for _ in range(n)]
        ans = 0
        def f(black_lengths, col):
            nonlocal ans
            if col == n:
                score = 0
                for c in range(1,n-1):
                    top = black_lengths[c]
                    left_right = max(black_lengths[c-1],black_lengths[c+1])
                    if top < left_right:
                        for k in range(top,left_right):
                            score += grid[k][c]

                top = black_lengths[0]
                left_right = black_lengths[1]
                if top < left_right:
                    for k in range(top,left_right):
                        score += grid[k][0]
                
                top = black_lengths[n-1]
                left_right = black_lengths[n-2]
                if top < left_right:
                    for k in range(top, left_right):
                        score += grid[k][n-1]
                ans = max(ans, score)
                return
            for r in range(n+1):
                black_lengths[col] = r
                f(black_lengths, col + 1)
        
        for r in range(n+1):
            black_lengths[0] = r
            f(black_lengths, 1)
        return ans


        # Brute recursive solution (O(R^2 * C * R^2) ultimately too slow where the first R^2 and C comes from 
        # necessary iteration)
        n = len(grid)
        if n == 1:
            return 0

        def recurse(prev_prev_i, prev_i, ind):
            if ind == n:
                col_contrib = 0
                for k in range(n):
                    if (prev_prev_i > k) and (prev_i <=k):
                        col_contrib += grid[k][ind-1]
                return col_contrib

            # n+1 denotes full colouring, 0 denotes completely white
            best = 0
            for i in range(n+1):
                # ind-1 column contribution:
                col_contrib = 0
                for k in range(n):
                    if (prev_prev_i > k or i > k) and (prev_i <= k):
                        col_contrib += grid[k][ind-1]

                score = recurse(prev_i, i, ind+1) + col_contrib
                best = max(best, score)
            return best
        
        ans = 0
        # Col 0
        for i1 in range(n+1):
            # Col 1
            for i2 in range(n+1):
                col_contrib = 0
                for k in range(n):
                    if (i2 > k) and (i1 <= k):
                        col_contrib += grid[k][0]                    
                ans = max(ans, recurse(i1, i2, 2) + col_contrib)

        return ans
        """

        # Incorporating prefix sums for O(1) column value computation, still too slow. Now is O(R^2 * C * R)
        n = len(grid)
        if n == 1:
            return 0

        column_sums = [sum([grid[i][j] for i in range(n)]) for j in range(n)]

        prefix_values = [[0 for _ in range(n)] for _ in range(n+1)]
        for j in range(n):
            for i in range(1, n+1):
                prefix_values[i][j] = prefix_values[i-1][j] + grid[i-1][j]   

        suffix_values = [[0]*n for _ in range(n+1)]
        for j in range(n):
            for i in range(n-1, -1, -1):
                suffix_values[i][j] = suffix_values[i+1][j] + grid[i][j]

        def recurse(prev_prev_i, prev_i, ind):
            if ind == n:
                if prev_i >= prev_prev_i:
                    return 0
                else:
                    return column_sums[ind-1] - prefix_values[prev_i][ind-1] - suffix_values[prev_prev_i][ind-1]

            # n+1 denotes full colouring, 0 denotes completely white
            best = 0
            for i in range(n+1):
                # ind-1 column contribution:
                if prev_i >= max(prev_prev_i, i):
                    col_contrib = 0
                else:
                    col_contrib = column_sums[ind-1] - prefix_values[prev_i][ind-1] - suffix_values[max(prev_prev_i,i)][ind-1]
                score = recurse(prev_i, i, ind+1) + col_contrib
                best = max(best, score)
            return best
        
        ans = 0
        # Col 0
        for i1 in range(n+1):
            # Col 1
            for i2 in range(n+1):
                col_contrib = 0
                for k in range(n):
                    if (i2 > k) and (i1 <= k):
                        col_contrib += grid[k][0]                    
                ans = max(ans, recurse(i1, i2, 2) + col_contrib)

        return ans


# Optimal solution with on the fly column contribution computation
class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        prev_col_w = [0] * (n+1) # [DP] prev col with prev col's score
        prev_col_wo = [0] * (n+1) # [DP] prev col without prev col's score
        if n == 1:
            return 0

        for j in range(1, n): # [LOOP] for each col
            cur_col_w = [0] * (n+1) # [DP] cur col with cur col's score
            cur_col_wo = [0] * (n+1) # [DP] cur col without cur col's score

            for i in range(n+1): # [LOOP] prev col (j-1) is black from row 0 to row i-1 (no black when i == 0)
                prev_col_val = 0 # prev col (j-1) score when prev black is i and cur black is k
                cur_col_val = 0 # cur col (j) score when prev black is i and cur black is k

                for p in range(i):
                    cur_col_val += grid[p][j]

                for k in range(n+1): # [LOOP] cur col (j) black is from row 0 to row k-1 (no black when k == 0)
                    if k > 0 and k <= i:
                        cur_col_val -= grid[k-1][j]
                    if k > i:
                        prev_col_val += grid[k-1][j-1]
                    cur_col_wo[k] = max(cur_col_wo[k], prev_col_val + prev_col_wo[i])
                    cur_col_wo[k] = max(cur_col_wo[k], prev_col_w[i])
                    cur_col_w[k] = max(cur_col_w[k], cur_col_val + prev_col_w[i])
                    cur_col_w[k] = max(cur_col_w[k], cur_col_val + prev_col_val + prev_col_wo[i])
                    
            prev_col_w = cur_col_w
            prev_col_wo = cur_col_wo
        return max(cur_col_w)