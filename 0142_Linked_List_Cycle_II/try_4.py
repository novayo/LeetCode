# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        hare = tortoise = head
        
        # Go to meet point
        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            
            if hare == tortoise:
                break
        
        # If no cycle
        if hare != tortoise:
            return None
        
        # Start from start point again
        hare = head
        while hare != tortoise:
            hare = hare.next
            tortoise = tortoise.next
        
        return hare

