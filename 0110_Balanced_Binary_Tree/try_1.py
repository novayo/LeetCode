# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        flag = False
        def dfs(node):
            nonlocal flag
            if flag:
                return 0
            
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if abs(left - right) <= 1:
                return max(left, right) + 1
            else:
                flag = True
                return 0
        
        dfs(root)
        return flag == False
