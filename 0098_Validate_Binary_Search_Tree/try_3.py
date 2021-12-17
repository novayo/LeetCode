# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        ans = False
        
        def dfs(node):
            nonlocal ans
            
            if ans:
                return 0, 0
            
            if not node:
                return float('inf'), -float('inf')
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if not (left[1] < node.val < right[0]):
                ans = True
                return 0, 0
            
            return min(left[0], node.val), max(right[1], node.val)
            
        dfs(root)
        return not ans
