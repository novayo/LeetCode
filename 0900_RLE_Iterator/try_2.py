class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.idx = 0
        self.encoding = encoding

    def next(self, n: int) -> int:
        remain = n
        while self.idx < len(self.encoding) and remain > 0:
            if remain > self.encoding[self.idx]:
                remain -= self.encoding[self.idx]
                self.idx += 2
            else:
                self.encoding[self.idx] -= remain
                remain = 0
        
        if self.idx >= len(self.encoding):
            return -1
        return self.encoding[self.idx+1]

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
