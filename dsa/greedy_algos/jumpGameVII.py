class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        if s[0] == "1":
            return False
        
        # BFS: Keep adding coordinates in the queue to explore
        queue = deque([0])
        # Greedy idea: We can simply look at max(i + minJump, mx + 1)
        # instead of i + minJump as our lower bound for every i since 
        # we want to avoid adding things again, hence despite being BFS
        # we do not need a visited array.
        mx = 0
        while queue:
            i = queue.popleft()
            for j in range(max(i + minJump, mx + 1), min(i + maxJump + 1, len(s))):
                if s[j] == '0':
                    if j == len(s) - 1: 
                        return True
                    queue.append(j)

            mx = i + maxJump
        return False