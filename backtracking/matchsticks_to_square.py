class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # subset-sum partition problem
        # Backtracking (Iterates through every solution)
        # Not divisible by 4
        """
        if sum(matchsticks) % 4 != 0:
            return False
        
        sides = [0] * 4
        
        def dfs(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]
            
            for side in range(4):
                sides[side] += matchsticks[i]
                if dfs(i + 1):
                    return True
                sides[side] -= matchsticks[i]
            
            return False
        
        return dfs(0)
        """

        # Backtracking with pruning
        """
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False
        
        length = total_length // 4
        sides = [0] * 4
        # Reverse sort to catch pruning early
        matchsticks.sort(reverse=True)
        
        def dfs(i):
            if i == len(matchsticks):
                return True
            
            for side in range(4):
                if sides[side] + matchsticks[i] <= length:
                    sides[side] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[side] -= matchsticks[i]
                
                # Pruning step, stops trying matchstick i.
                if sides[side] == 0:
                    break
        
            return False

        return dfs(0)
        """

        # Dynamic programming (Bit mask)
        # Key concept: We try building the square in reverse by considering 
        # building it with smaller subsets of the matchsticks set then adding on sticks

        # Early impossible case handling
        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False
        length = total_length // 4
        if max(matchsticks) > length:
            return False
        
        # Number of matchsticks
        n = len(matchsticks)

        # An array to store the current progress on the current side for a given subset of used matchsticks 
        # Every index corresponds to a subset and -inf denotes unvisited.
        # We assume converting an index "mask" to binary gives the representation 
        # of which matchsticks are included and not in the subset. 
        # E.g. 3=101 which means mask=3 corresponds to having 
        # matchsticks 0 and 2

        # The memoization here is that we are trying to recursively build up the sides by 
        # seeing what sequence of choices of sticks to choose gets us to forming a square
        # if possible.
        dp = [float("-inf")] * (1 << n)
        matchsticks.sort(reverse=True)

        def dfs(mask):
            if mask == 0:
                return 0 # No matchsticks left to remove, so progress/running mod length sum is 0
            
            # If already computed reuse the value
            if dp[mask] != float("-inf"):
                return dp[mask] 
            

            for i in range(n):
                # Check if the matchstick is in the current subset
                if mask & (1 << i):

                    # Try removing matchstick i using mask ^ (1<<i) and running dfs again.
                    # Builds recursive depth till we reach the last matchstick
                    res = dfs(mask ^ (1 << i)) 

                    # If we can add on matchstick i, add it and this is the progress
                    if res >= 0 and res + matchsticks[i] <= length:
                        # Either builds on existing side or goes to new one
                        dp[mask] = (res + matchsticks[i]) % length
                        # Either 0 or some int between 0 and length.
                        return dp[mask]
                    
                    # If the mask includes everything
                    # Mark the length as -1 to indicate subset is invalid
                    if mask == (1 << n) - 1:
                        dp[mask] = -1
                        return -1
            
            # If nothing works in adding another matchstick
            # then our current inclusion sequence is a failing sequence
            dp[mask] = -1
            return -1
        
        # Start with all set to 1
        # If everything works properly, 
        # then the dfs returns 0, so not 0 is True.
        return not dfs((1 << n) - 1)