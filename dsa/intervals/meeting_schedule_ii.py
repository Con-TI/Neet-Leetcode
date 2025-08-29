"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Minheap
        intervals.sort(key = lambda x: x.start)
        min_heap = []
        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)

        # Two ptrs
        # Line sweep using two ptrs
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)
        res = count = 0
        s = e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res
        
        # Greedy (line sweep)

        # +1 means a meeting starts
        # -1 means a meeting ends
        time = []
        for i in intervals:
            time.append((i.start, 1))
            time.append((i.end,-1))

        time.sort(key = lambda x: (x[0], x[1]))
        
        # count keeps track of the running meetings at any one time
        # res is the running total
        # If there were a max of i amount of meetings, then intuitively we need
        # i days.
        res = count = 0
        for t in time:
            count += t[1]
            res = max(res, count)
        return res