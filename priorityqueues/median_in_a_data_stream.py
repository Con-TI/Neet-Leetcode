class MedianFinder:

    def __init__(self):
        # Heaps
        # small keeps track of smaller half
        # large keeps track of bigger half
        # Median is now easy to calculate, either top of small, bottom of large, or average.
        self.small, self.large = [], []
        

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            # Allows pop to call smallest nums in large
            heapq.heappush(self.large, num)
        else:
            # Allows for pop to call the biggest nums (in abs terms) in small
            heapq.heappush(self.small, -1*num)

        # If the sizes are unbalanced
        ## adjusted so other list gets appended if diff is 1 or larger
        ## Takes advantage of heap pop properties to quickly remove and add 
        ## the middle numbers.
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # If unequal sizes
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        # If equal sizes
        return (-1 * self.small[0] + self.large[0]) / 2.0