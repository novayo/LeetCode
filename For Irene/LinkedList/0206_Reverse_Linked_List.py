# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        dummy = ListNode(-1)
        dummy.next = head
        
        tmp = head.next
        while tmp != None:
            head.next = tmp.next
            tmp.next = dummy.next
            dummy.next = tmp
            tmp = head.next
        
        return dummy.next