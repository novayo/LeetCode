class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.sortedStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.sortedStack.insert(bisect.bisect_left(self.sortedStack, x), x)
        
    def pop(self) -> None:
        # self.sortedStack.remove(self.stack.pop()) # O(n)
        del self.sortedStack[bisect.bisect_left(self.sortedStack, self.stack.pop())] # O(logn)
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.sortedStack[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
