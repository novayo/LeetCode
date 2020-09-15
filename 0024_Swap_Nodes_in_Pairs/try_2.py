# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        def swap(node):
            tmp = node.next
            node.next = node.next.next
            tmp.next = node
            return tmp
        
        def recr(node):
            if not node or not node.next:
                return node
            
            node = swap(node)
            node.next.next = recr(node.next.next)
            return node
        
        head = recr(head)
        return head
