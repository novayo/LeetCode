# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        
        def recr(node):
            if not node:
                return None, None
            
            if node.val <= target:
                low, high = recr(node.right)
                node.right = low
                return node, high
            else:
                low, high = recr(node.left)
                node.left = high
                return low, node
        
        return recr(root)
