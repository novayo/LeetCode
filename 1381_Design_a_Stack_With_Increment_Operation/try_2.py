class CustomStack:

    # maxSize: capacity
    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.inc = collections.defaultdict(int)

    def push(self, x: int) -> None:
        # if over => don't push
        if len(self.stack) >= self.maxSize:
            return
        
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        
        i = len(self.stack)
        ret = self.stack.pop()
        inc = self.inc[i]
        
        del self.inc[i]
        if i > 0:
            self.inc[i-1] += inc
        
        return ret + inc

    def increment(self, k: int, val: int) -> None:
        # 前k個都加上val -> k可以超過
        self.inc[min(k, len(self.stack))] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)