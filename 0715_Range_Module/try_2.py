class RangeModule:

    def __init__(self):
        self.arr = []

    def addRange(self, left: int, right: int) -> None:
        s = bisect.bisect_left(self.arr, left)
        e = bisect.bisect_right(self.arr, right)
        
        _slice = []
        if s % 2 == 0:
            _slice.append(left)
        if e % 2 == 0:
            _slice.append(right)
        
        self.arr[s:e] = _slice

    def queryRange(self, left: int, right: int) -> bool:
        s = bisect.bisect_right(self.arr, left)
        e = bisect.bisect_left(self.arr, right)
        
        # 完全overlap
        return s == e and s % 2 == 1
    
        # 完全沒有overlap
        return s == e and s % 2 == 0
    
        # 不 完全沒有overlap
        return not (s == e and s % 2 == 0)

    def removeRange(self, left: int, right: int) -> None:
        s = bisect.bisect_left(self.arr, left)
        e = bisect.bisect_right(self.arr, right)
        
        _slice = []
        if s % 2 == 1:
            _slice.append(left)
        if e % 2 == 1:
            _slice.append(right)
        
        self.arr[s:e] = _slice


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)