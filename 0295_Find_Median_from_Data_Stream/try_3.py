class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def addNum(self, num: int) -> None:
        index = bisect.bisect_left(self.arr, num)
        self.arr.insert(index, num)

    def findMedian(self) -> float:
        n = len(self.arr)//2
        if len(self.arr) % 2 == 1:
            return self.arr[n]
        else:
            return (self.arr[n-1] + self.arr[n]) / 2
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()