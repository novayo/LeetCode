# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        '''
        three choices
        1: root
        2: x.left
        3: x.right
        '''
        
        root_num = x_left = x_right = 0
        
        def dfs(node):
            nonlocal root_num, x_left, x_right
            
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.val == x:
                x_left = left
                x_right = right
                return 0
            else:
                return left + right + 1
        
        root_num = dfs(root)
        
        
        if x_left + x_right + 1 < root_num or \
           x_left + root_num + 1 < x_right or \
           x_right + root_num + 1 < x_left:
            return True
        else:
            return False
        
