class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or self.min_stack[-1][0] > x:
            self.min_stack.append([x,1])
        elif self.min_stack[-1][0] == x:
            self.min_stack[-1][1] += 1

    def pop(self) -> None:
        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack[-1][1] -= 1
        
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
