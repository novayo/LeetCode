# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        found = set()
        def recr(node):
            nonlocal found
            
            if not node:
                return False
            
            if k - node.val in found:
                return True
            
            found.add(node.val)
            
            if recr(node.left):
                return True
            if recr(node.right):
                return True
            return False
        
        return recr(root)

