# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        MARK = 'x'
        ptr = head
        
        while ptr and ptr.val != MARK:
            ptr.val = MARK
            ptr = ptr.next
        
        return ptr
