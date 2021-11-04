# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        start = end = dummy
        
        while n:
            end = end.next
            n -= 1
        
        while end and end.next:
            start = start.next
            end = end.next
        
        start.next = start.next.next
        return dummy.next