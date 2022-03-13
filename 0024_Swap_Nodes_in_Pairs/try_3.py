# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = dummy = ListNode()
        dummy.next = head
        
        while a.next and a.next.next:
            b = a.next
            c = a.next.next
            
            b.next = c.next
            c.next = a.next
            a.next = c
            a = a.next.next
            
        return dummy.next
    
