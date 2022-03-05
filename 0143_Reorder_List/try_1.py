# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        tmp = head
        while tmp:
            stack.append(tmp)
            tmp = tmp.next
            stack[-1].next = None
        
        if len(stack) == 1:
            return head
        
        head.next = stack[-1]
        tmp = stack[-1]
        i, j = 1, len(stack)-2
        while i <= j:
            if i == j:
                tmp.next = stack[i]
            else:
                tmp.next = stack[i]
                stack[i].next = stack[j]
                tmp = stack[j]
            i, j = i+1, j-1
        return head
