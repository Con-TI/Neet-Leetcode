class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # Sorting brute force
        # self.k = k
        # self.arr = nums

        # Minimum heap
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Sorting brute force
        # self.arr.append(val)
        # self.arr.sort()
        # return self.arr[-self.k]

        # Minimum heap
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]