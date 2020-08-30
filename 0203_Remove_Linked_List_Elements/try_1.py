# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        '''
        看下一個值，
        等於val就remove，
        等於None就停止
        '''
        if not head:
            return None
        
        newHead = ListNode(-1)
        newHead.next = head
        
        tmp = newHead
        while tmp.next:
            if tmp.next.val == val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return newHead.next
