class Node:
    def __init__(self, val=-1, pre=None, next=None):
        self.val = val
        self.pre = pre
        self.next = next

class CustomStack:

    def __init__(self, maxSize: int):
        self.head = self.tail = Node()
        self.maxSize = maxSize
        self.curSize = 0

    def push(self, x: int) -> None:
        if self.curSize >= self.maxSize:
            return
        
        self.tail.next = Node(x)
        self.tail.next.pre = self.tail
        self.tail = self.tail.next
        self.curSize += 1

    def pop(self) -> int:
        if self.curSize == 0:
            return -1
        
        ret = self.tail.val
        
        self.tail = self.tail.pre
        self.tail.next = None
        self.curSize -= 1
        
        return ret

    def increment(self, k: int, val: int) -> None:
        tmp = self.head
        
        while k > 0 and tmp.next:
            tmp = tmp.next
            tmp.val += val
            k -= 1

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)