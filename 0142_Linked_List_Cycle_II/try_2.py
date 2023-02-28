# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cache = set()
        
        ptr = head
        while ptr and ptr not in cache:
            if ptr not in cache:
                cache.add(ptr)
            ptr = ptr.next

        return ptr
