# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        
        # Init
        node_i = node_j = dummy
        for _ in range(n):
            node_j = node_j.next
        
        # Run to the end
        while node_j and node_j.next:
            node_i = node_i.next
            node_j = node_j.next
        
        # Remove nth node
        node_i.next = node_i.next.next
        
        return dummy.next

