class Node:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node()
    
    def printNode(self):
        ptr = self.head
        while ptr:
            print(ptr.val, end="->")
            ptr = ptr.next
        print()
    
    # O(n)
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        ptr = self.head
        for i in range(index+1):
            if not ptr:
                break
            ptr = ptr.next
        
        if not ptr:
            return -1
        return ptr.val
        
    # O(1)
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        tmp = self.head.next
        self.head.next = Node(val, tmp)
        
    # O(n)
    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        ptr = self.head
        while ptr and ptr.next:
            ptr = ptr.next
        
        ptr.next = Node(val)
        
    # O(n)
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        ptr = self.head
        for i in range(index):
            if not ptr:
                break
            ptr = ptr.next
        
        if not ptr:
            return
        
        tmp = ptr.next
        ptr.next = Node(val, tmp)
        
    # O(n)
    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        ptr = self.head
        for i in range(index):
            if not ptr:
                break
            ptr = ptr.next
        
        if not ptr:
            return
        
        if ptr and ptr.next:
            ptr.next = ptr.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)