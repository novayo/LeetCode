# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        cur = odd_last = head
        even = even_last = head.next
        
        while even_last and even_last.next:
            cur = even_last.next
            even_last.next = cur.next
            cur.next = even
            odd_last.next = cur
            
            odd_last = odd_last.next
            even_last = even_last.next
            
        
        return head