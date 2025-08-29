class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        returnedintervals = [intervals[0]]

        for i2 in intervals:
            i1 = returnedintervals.pop()
            if i1[0] > i2[1]:
                returnedintervals.append(i2)
                returnedintervals.append(i1)
            elif i2[0] > i1[1]:
                returnedintervals.append(i1)
                returnedintervals.append(i2)
            else:
                i1 = [min(i1[0], i2[0]), max(i1[1], i2[1])]
                returnedintervals.append(i1)
        return returnedintervals 