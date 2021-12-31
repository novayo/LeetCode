# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        def dfs(node):
            
            if not node:
                return 1
            
            node.val += dfs(node.next)
            
            carry = 0
            if node.val >= 10:
                node.val -= 10
                carry = 1
            
            return carry
        
        carry = dfs(head)
        if carry == 1:
            return ListNode(1, head)
        else:
            return head
            
