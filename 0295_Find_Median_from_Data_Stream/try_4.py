class MedianFinder:

    def __init__(self):
        self.larger = [] # min-heap
        self.smaller = [] # max-heap

    def addNum(self, num: int) -> None:
        nlarger = len(self.larger)
        nsmaller = len(self.smaller)
        
        if nlarger == nsmaller:
            if self.larger and num >= self.larger[0]:
                heapq.heappush(self.smaller, -heapq.heappop(self.larger))
                heapq.heappush(self.larger, num)
            else:
                heapq.heappush(self.smaller, -num)
                
        elif nlarger < nsmaller:
            if num <= -self.smaller[0]:
                heapq.heappush(self.larger, -heapq.heappop(self.smaller))
                heapq.heappush(self.smaller, -num)
            else:
                heapq.heappush(self.larger, num)

    def findMedian(self) -> float:
        if len(self.larger) < len(self.smaller):
            return -self.smaller[0]
        elif len(self.larger) == len(self.smaller):
            return (self.larger[0] + (-self.smaller[0])) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()