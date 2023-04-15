# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def recr(node):
            if not node:
                return 0
            
            ret = 0
            if not (node.val < low):
                ret += recr(node.left)
            
            if not (node.val > high):
                ret += recr(node.right)
            
            if low <= node.val <= high:
                ret += node.val
            
            return ret
        
        return recr(root)