# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        
        ptr = head
        while ptr and ptr.next:
            tmp = ptr.next
            ptr.next = ptr.next.next
            tmp.next = dummy.next
            dummy.next = tmp
        return dummy.next

