class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # min heap
        # trips.sort(key = lambda t: t[1])
        # minHeap = []
        # curPass = 0
        # for numPass, start, end in trips:
        #     while minHeap and minHeap[0][0] <= start:
        #         # Remove numPass as the trip has finished
        #         curPass -= heapq.heappop(minHeap)[1]
            
        #     curPass += numPass
        #     if curPass > capacity:
        #         return False
            
        #     heapq.heappush(minHeap, [end, numPass])
        
        # return True

        # Line sweep
        L, R = float("inf"), float("-inf")
        for _, start, end in trips:
            L = min(L, start)
            R = max(R, end)
        
        # Time points
        N = R - L + 1
        passChange = [0] * (N + 1)

        # Picking up and removing passengers
        for passengers, start, end in trips:
            passChange[start - L] += passengers
            passChange[end - L] -= passengers
        
        curPass = 0
        # Go through the changes
        for change in passChange:
            curPass += change
            # If the number of passengers ever exceeds limit, False
            if curPass > capacity:
                return False
        
        return True