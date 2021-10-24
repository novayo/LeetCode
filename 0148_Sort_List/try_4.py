# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def findMid(node):
            t = None
            while node and node.next:
                t = node if not t else t.next
                node = node.next.next
            ret = t.next
            t.next = None
            return ret
        
        def merge(start):
            if not start or not start.next:
                return start
            
            mid = findMid(start)
            left = merge(start)
            right = merge(mid)
            
            tmp = dummy = ListNode(0)
            while left and right:
                if left.val <= right.val:
                    tmp.next = left
                    left = left.next
                else:
                    tmp.next = right
                    right = right.next
                tmp = tmp.next
                    
            if left:
                tmp.next = left
            
            if right:
                tmp.next = right
                
            return dummy.next
        
        return merge(head)
            