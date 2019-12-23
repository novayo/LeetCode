# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head: return False
        tmp = head
        while tmp.val != -float('inf'):
            tmp.val = -float('inf')
            tmp = tmp.next
            if not tmp:
                return False
        
        return True
