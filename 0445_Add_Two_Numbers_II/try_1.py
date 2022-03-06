# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse_list(l1)
        l2 = self.reverse_list(l2)
        
        ans = tmp = ListNode()
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            tmp.next = ListNode(carry%10)
            tmp = tmp.next
            carry //= 10
        return self.reverse_list(ans.next)
        
    def reverse_list(self, linked):
        dummy = ListNode()
        dummy.next = pt = linked
        
        while pt and pt.next:
            tmp = pt.next
            pt.next = pt.next.next
            tmp.next = dummy.next
            dummy.next = tmp
        
        return dummy.next
