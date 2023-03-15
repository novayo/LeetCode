class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.inc_map = collections.defaultdict(int)
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) >= self.maxSize:
            return
        
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        
        inc = self.inc_map[len(self.stack)]
        del self.inc_map[len(self.stack)]
        
        ret = self.stack.pop() + inc
        if len(self.stack) > 0:
            self.inc_map[len(self.stack)] += inc
        
        return ret

    def increment(self, k: int, val: int) -> None:
        self.inc_map[min(k, len(self.stack))] += val

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
