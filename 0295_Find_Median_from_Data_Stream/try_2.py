class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.larger = []    # min-heap
        self.smaller = []   # max-heap
        
    def addNum(self, num: int) -> None:
        # push into larger and pop min
        n = heapq.heappushpop(self.larger, -num)
        
        # push into smaller
        heapq.heappush(self.smaller, -n)
        
        # maintain two heap
        if len(self.larger) < len(self.smaller):
            heapq.heappush(self.larger, -heapq.heappop(self.smaller))

    def findMedian(self) -> float:
        if (len(self.larger) + len(self.smaller)) % 2 == 0:
            return round((self.smaller[0] + -self.larger[0])/2, 5)
        else:
            return round(-self.larger[0], 5)
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()