# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        if tmp == []: return head
        
        tmp.sort()
        
        ans = t = ListNode(tmp[0])
        for i in tmp[1:]:
            t.next = ListNode(i)
            t = t.next
        
        return ans
