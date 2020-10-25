class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        while self.queue1:
            self.queue2.appendleft(self.queue1.pop())
        
        self.queue1.appendleft(x)
        
        while self.queue2:
            self.queue1.appendleft(self.queue2.pop())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue1.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue1[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.queue1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
