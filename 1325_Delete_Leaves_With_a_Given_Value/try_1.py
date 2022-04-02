# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def recr(node):
            if not node:
                return None
            
            node.left = recr(node.left)
            node.right = recr(node.right)
            
            if node.val == target and not node.left and not node.right:
                return None
            else:
                return node
        
        return recr(root)
