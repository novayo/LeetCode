class Node:
    def __init__(self, val=-1, next=None, pre=None):
        self.val = val
        self.next = next
        self.pre = pre
        
class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.current_size = 0
        self.head = self.tail = Node()

    def push(self, x: int) -> None:
        if self.current_size >= self.maxSize:
            return
        
        self.tail.next = Node(x, pre=self.tail)
        self.tail = self.tail.next
        self.current_size += 1

    def pop(self) -> int:
        if self.current_size == 0:
            return -1
        
        ret = self.tail.val
        self.tail = self.tail.pre
        self.tail.next = None
        self.current_size -= 1
        return ret

    def increment(self, k: int, val: int) -> None:
        head = self.head
        
        while head.next and k:
            head = head.next
            head.val += val
            k -= 1


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)