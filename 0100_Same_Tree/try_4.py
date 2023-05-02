# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recr(node, container):
            if not node:
                container.append(None)
                return
            
            container.append(node.val)
            recr(node.left, container)
            recr(node.right, container)
        
        left_values = []
        right_values = []
        recr(p, left_values)
        recr(q, right_values)
        return left_values == right_values
