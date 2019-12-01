# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        oddHead = tmpOddHead = ListNode(0)
        evenHead = tmpEvenHead = ListNode(0)
        
        while head:
            tmpOddHead.next = head
            tmpEvenHead.next = head.next
            tmpOddHead = tmpOddHead.next
            tmpEvenHead = tmpEvenHead.next
            head = head.next.next if tmpEvenHead != None else None
        tmpOddHead.next = evenHead.next
        return oddHead.next
