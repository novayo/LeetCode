# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp_odd = odd = ListNode()
        tmp_even = even = ListNode()
        
        a = ListNode()
        a.next = head
        
        isOdd = True
        while a and a.next:
            b = a.next
            a.next = None
            a = b
            
            
            if isOdd:
                tmp_odd.next = b
                tmp_odd = tmp_odd.next
            else:
                tmp_even.next = b
                tmp_even = tmp_even.next
            isOdd = not isOdd
            
        tmp_odd.next = even.next
        return odd.next
