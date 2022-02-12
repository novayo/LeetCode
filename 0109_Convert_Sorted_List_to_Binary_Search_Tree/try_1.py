# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        def find_mid(head):
            pre_tortoise = None
            hare = tortoise = head
            while hare and hare.next:
                pre_tortoise = tortoise
                tortoise = tortoise.next
                hare = hare.next.next
            return pre_tortoise, tortoise
        
        def recr(head):
            if not head:
                return None
            pre_mid, mid = find_mid(head)
            
            root = TreeNode(mid.val)
            
            if mid == head:
                return root
            
            pre_mid.next = None
            root.left = recr(head)
            root.right = recr(mid.next)
            pre_mid.next = mid
            return root
        
        return recr(head)

