# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        found_flag = False
        def top_down(node, curSum):
            nonlocal found_flag
            
            if found_flag:
                return
            
            if not node:
                return
            
            curSum += node.val
            if not node.left and not node.right and curSum == targetSum:
                found_flag = True
                return
            
            top_down(node.left, curSum)
            top_down(node.right, curSum)
        
        top_down(root, 0)
        return found_flag
