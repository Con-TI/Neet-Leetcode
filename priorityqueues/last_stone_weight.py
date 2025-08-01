class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Heap
        minHeap = [-w for w in stones]
        heapq.heapify(minHeap)
        
        while len(minHeap) > 1:
            x, y = heapq.heappop(minHeap), heapq.heappop(minHeap)
            if x==y:
                continue
            if x < y:
                heapq.heappush(minHeap, -(abs(x)-abs(y)))
            else:
                heapq.heappush(minHeap, -(abs(y)-abs(x)))

        if minHeap:
            return -minHeap[0]
        return 0

        # Bucket sort
        maxStone = max(stones)
        bucket = [0] * (maxStone + 1)
        for stone in stones:
            bucket[stone] += 1
        

        first = second = maxStone
        while first > 0:
            # x=y
            if bucket[first] % 2 == 0:
                first -= 1
                continue
            
            # x!=y
            j = min(first - 1, second)
            while j > 0 and bucket[j] == 0:
                j -= 1
            
            # No stones left
            if j == 0:
                return first

            second = j
            # first > second
            bucket[first] -= 1
            bucket[second] -= 1
            bucket[first - second] += 1
            # Adjust first
            first = max(first - second, second)
        return first