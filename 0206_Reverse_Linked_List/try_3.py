# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        把下個值都往頭丟
        '''
        
        if not head:
            return None
        
        tmp = head
        while tmp.next:
            target = tmp.next
            tmp.next = target.next
            target.next = head
            head = target
        return head
