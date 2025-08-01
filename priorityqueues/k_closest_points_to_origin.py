class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Minheap
        minHeap = []
        for x,y in points:
            dist = x**2 + y**2
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        res = []
        while k>0:
            # Python compares each heap entry lexicographically (from index 0)
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1
        
        return res

        # Max heap
        maxHeap = []
        for x,y in points:
            dist = -x**2 - y**2
            heapq.heappush(maxHeap, [dist,x,y])
            if len(maxHeap) > k:
                # Effectively removes the larger elements
                heapq.heappop(maxHeap)
            
        res = []
        while maxHeap:
            dist,x,y = heapq.heappop(maxHeap)
            res.append([x,y])

        return res