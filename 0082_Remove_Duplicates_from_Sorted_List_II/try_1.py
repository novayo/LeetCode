# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        s = dummy = ListNode()
        a = dummy.next = head
        
        while a:
            count = 0
            b = a
            while b and b.val == a.val:
                count += 1
                b = b.next
            
            if count == 1:
                s.next = a
                s = s.next
            
            a = b
        
        s.next = None
        return dummy.next