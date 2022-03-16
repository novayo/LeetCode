class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k+1
        self.queue = [0] * self.k
        self.front = self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = self.nextI(self.rear)
        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = self.nextI(self.front)
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.nextI(self.front)]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.rear == self.front

    def isFull(self) -> bool:
        return self.nextI(self.rear) == self.front
    
    def nextI(self, i):
        return (i+1) % self.k
    
    def preI(self, i):
        return i-1 if i > 0 else self.k-1


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()