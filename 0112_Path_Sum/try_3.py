# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        def top_down(node, sum):
            if not node:
                return False
            
            sum -= node.val
            if not node.left and not node.right:
                return sum == 0
            
            return top_down(node.left, sum) or top_down(node.right, sum)
        
        return top_down(root, sum)
