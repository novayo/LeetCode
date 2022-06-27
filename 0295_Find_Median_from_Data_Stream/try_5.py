class MedianFinder:

    def __init__(self):
        self.n = 0
        self.larger = []  # min heap
        self.smaller = [] # max heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.larger, num)
        heapq.heappush(self.smaller, -heapq.heappop(self.larger))
        
        if len(self.smaller) > len(self.larger):
            heapq.heappush(self.larger, -heapq.heappop(self.smaller))

        self.n += 1

    def findMedian(self) -> float:
        if self.n % 2 == 1:
            return self.larger[0]
        else:
            return (self.larger[0] - self.smaller[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
