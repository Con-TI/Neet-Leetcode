class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        minHeap = []
        res = {}
        i = 0
        for q in sorted(queries):
            # Look at all intervals whose left bound is less than q
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minHeap, (r - l + 1,r))
                i += 1

            # Remove all intervals whose right bound is also less than q
            while minHeap and minHeap[0][1] < q:
                heapq.heappop(minHeap)
            
            # If there is anything remaining in the minHeap, it automatically 
            # satisfies interval[0] <= q <= interval[1] 
            # and is of shortest length
            res[q] = minHeap[0][0] if minHeap else -1

            # We do not reset the minHeap since we've sorted the queries
        
        # Returns a sorted list based on the order of queries
        return [res[q] for q in queries]