class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.idx = 0

    def next(self, n: int) -> int:
        ret = -1
        while n > 0 and self.idx < len(self.encoding):
            if n <= self.encoding[self.idx]:
                self.encoding[self.idx] -= n
                n = 0
                ret = self.encoding[self.idx+1]
            else:
                n -= self.encoding[self.idx]
                self.encoding[self.idx] = 0
                ret = self.encoding[self.idx+1]
            
            while self.idx < len(self.encoding) and self.encoding[self.idx] == 0:
                self.idx += 2
                
        
        if n > 0 and self.idx >= len(self.encoding):
            return -1
        return ret


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)
