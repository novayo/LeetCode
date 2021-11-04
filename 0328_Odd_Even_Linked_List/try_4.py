# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        # get end
        count = 2
        preend = end = head
        end = end.next
        while end and end.next:
            preend = end
            end = end.next
            count += 1
        
        if count % 2 == 0:
            last = end
            end = preend

        # loop
        start = head
        tmp = end
        while start != end:
            t = start.next
            start.next = t.next
            tmp.next = t
            t.next = None
            start = start.next
            tmp = tmp.next
        
        if count % 2 == 0:
            tmp.next = last
        return head