class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.ptr = 0
        self.occupy = 0

    def next(self, n: int) -> int:
        self.occupy += n
        while self.ptr < len(self.encoding) and self.occupy > self.encoding[self.ptr]:
            self.occupy -= self.encoding[self.ptr]
            self.ptr += 2
        
        if self.ptr >= len(self.encoding):
            return -1
        else:
            return self.encoding[self.ptr+1]


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)