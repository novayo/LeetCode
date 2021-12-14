# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        ans = True
        def dfs(node):
            nonlocal ans
            
            if ans == False:
                return 0
            
            if not node:
                return -1
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            if ans == False:
                return 0
            
            # TODO
            if abs(left_height - right_height) > 1:
                ans = False
                return 0
            
            return max(left_height, right_height) + 1
        
        dfs(root)
        return ans