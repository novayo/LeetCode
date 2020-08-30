class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(-1)
        self.head.next = Node(-1)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        tmp = self.head
        for i in range(index+1):
            tmp = tmp.next
            if tmp.val == -1:
                return -1
        return tmp.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        tmp = self.head
        newNode = Node(val)
        newNode.next = tmp.next
        tmp.next = newNode

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        tmp = self.head
        while tmp.next.val != -1:
            tmp = tmp.next
        newNode = Node(val)
        newNode.next = tmp.next
        tmp.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        tmp = self.head
        for i in range(index):
            if tmp.next.val == -1:
                return
            tmp = tmp.next
        newNode = Node(val)
        newNode.next = tmp.next
        tmp.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        tmp = self.head
        for i in range(index):
            if tmp.next.val == -1:
                return
            tmp = tmp.next

        if tmp.next.val == -1:
            return
        tmp.next = tmp.next.next if tmp.next else None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
