class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Highest weight
        m = max(people)
        
        # First two ptrs pass
        # Sorts weights from lowest to highest
        count = [0] * (m+1)
        for p in people:
            count[p] += 1
        idx,i = 0,1
        while idx < len(people):
            while count[i] == 0:
                i += 1
            people[idx] = i
            count[i] -= 1
            idx += 1


        # Second two ptrs pass
        # Adds boats by matching high weight with low weights.
        res, l, r = 0, 0, len(people) - 1        
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            # If you can fit a low weight, add them (Only one can be added by 2 person limit).
            if l <= r and remain >= people[l]:
                l += 1
        
        return res