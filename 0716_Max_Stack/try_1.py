class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        
        if not self.max_stack or self.max_stack[-1] < x:
            self.max_stack.append(x)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self) -> int:
        self.max_stack.pop()
        e = self.stack.pop()
        return e

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1]

    def popMax(self) -> int:
        e = self.max_stack[-1]
        tmp = []
        while self.max_stack[-1] != self.stack[-1]:
            tmp.append(self.pop())
        self.pop()
        while tmp:
            self.push(tmp.pop())
        return e

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()