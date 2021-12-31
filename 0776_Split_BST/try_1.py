# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        
        def dfs(node):
            if not node:
                return None, None
            elif node.val <= target:
                right = dfs(node.right)
                node.right = right[0]
                return node, right[1]
            else:
                left = dfs(node.left)
                node.left = left[1]
                return left[0], node
        
        return dfs(root)
