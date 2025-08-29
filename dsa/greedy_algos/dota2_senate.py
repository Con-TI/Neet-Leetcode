class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        n = len(senate)
        radiants = deque([])
        dires = deque([])

        for i,s in enumerate(senate):
            if s == "R":
                radiants.append(i)
            else:
                dires.append(i)


        while radiants and dires:
            r = radiants.popleft()
            d = dires.popleft()
            if r < d:
                radiants.append(r + n)
            else:
                dires.append(d + n)

        return "Radiant" if radiants else "Dire"
