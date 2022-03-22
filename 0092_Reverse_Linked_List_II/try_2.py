# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        visit_node = 0
        pre = dummy
        
        # find head
        my_head = None
        while visit_node < left - 1:
            pre = pre.next
            visit_node += 1
        
        my_head = pre
        pre = pre.next
        cur = pre.next
        
        while visit_node < right-1:
            
            pre.next = cur.next
            cur.next = my_head.next
            my_head.next = cur
            cur = pre.next
            
            visit_node += 1
        
        return dummy.next