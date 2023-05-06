# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def recr(node, curSum):
            if node is None:
                return False
            
            # visit
            curSum += node.val
            if node.left is None and node.right is None and curSum == targetSum:
                return True
        
            if recr(node.left, curSum):
                return True
            if recr(node.right, curSum):
                return True
            return False
        
        return recr(root, 0)
