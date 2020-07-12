# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # recursivey
        '''
        去recursive先去找到底，之後再慢慢的把答案從尾巴串接起來
        '''
        
        if not head:
            return None
        
        tmp = ans = ListNode(0)
        
        def recr(node):
            nonlocal tmp
            
            if node.next:
                recr(node.next)
            
            tmp.next = ListNode(node.val)
            tmp = tmp.next
        
        recr(head)
        return ans.next
