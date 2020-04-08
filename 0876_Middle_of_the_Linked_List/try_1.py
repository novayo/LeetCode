# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        tmp = head
        
        _len = 0
        while tmp:
            tmp = tmp.next
            _len += 1
        
        for _ in range(_len//2):
            head = head.next
        return head
