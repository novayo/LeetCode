# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        tmp = head
        while tmp and tmp.next:
            a = tmp.val
            tmp.val = tmp.next.val
            tmp.next.val = a
            tmp = tmp.next.next if tmp.next else None
        return head
