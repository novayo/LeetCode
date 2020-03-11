# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = tmp = ListNode(0)
        
        while l1 or l2:
            ttmp = 1
            if l1 and l2:
                if l1.val > l2.val:
                    ttmp = 2
            else:
                if l2:
                    ttmp = 2
            
            if ttmp == 1:
                tmp.next = ListNode(l1.val)
                tmp = tmp.next
                l1 = l1.next
            else:
                tmp.next = ListNode(l2.val)
                tmp = tmp.next
                l2 = l2.next
        return ans.next
