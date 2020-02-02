class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = collections.deque()

    def addNum(self, num: int) -> None:
        self.data.insert(bisect.bisect_left(self.data, num), num)

    def findMedian(self) -> float:
        _len = len(self.data) // 2
        return self.data[_len] if len(self.data) & 1 else (self.data[_len - 1] + self.data[_len]) * 0.5


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
