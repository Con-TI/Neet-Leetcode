class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        # Find the first and last interval in intervals
        # which contains newInterval
        newintervals = [newInterval]
        
        for interval in intervals:
            merge = newintervals.pop()
            if interval[1] < merge[0]:
                newintervals.append(interval)
                newintervals.append(merge)
            elif interval[0] > merge[1]:
                newintervals.append(merge)
                newintervals.append(interval)
            else:
                merge = [min(interval[0], merge[0]),max(interval[1], merge[1])]
                newintervals.append(merge)
            
        return list(newintervals)