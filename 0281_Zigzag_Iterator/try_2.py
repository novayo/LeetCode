class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.v = [v1, v2]
        self.n = len(self.v)
        self.index = 0
        self.index_in_v = [0] * self.n
        self.finished = [True] * self.n
        
        # init
        for i in range(self.n):
            v = self.v[i]
            if len(v) == 0:
                self.finished[i] = False
        
    def next(self) -> int:
        # find next
        self.index %= self.n
        while self.finished[self.index % self.n] == False:
            self.index += 1
        self.index %= self.n
        
        # find return value
        v = self.v[self.index]
        i = self.index_in_v[self.index]
        ret = v[i]
        
        # inc
        self.index_in_v[self.index] += 1
        if self.index_in_v[self.index] >= len(v):
            self.finished[self.index] = False
        self.index += 1
        
        return ret

    def hasNext(self) -> bool:
        return any(self.finished)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
