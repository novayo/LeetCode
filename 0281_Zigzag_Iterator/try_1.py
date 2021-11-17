class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v1 = v1
        self.v2 = v2
        self.i1 = 0
        self.i2 = 0
        self.turn = True # T: v1, F: v2

    def next(self) -> int:
        ret = -float('inf')
        
        if self.i1 >= len(self.v1):
            self.turn = False
        if self.i2 >= len(self.v2):
            self.turn = True
        
        if self.turn and self.i1 < len(self.v1):
            ret = self.v1[self.i1]
            self.i1 += 1
        elif not self.turn and self.i2 < len(self.v2):
            ret = self.v2[self.i2]
            self.i2 += 1
        
        self.turn = not self.turn
        return ret

    def hasNext(self) -> bool:
        return self.i1 < len(self.v1) or self.i2 < len(self.v2)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
