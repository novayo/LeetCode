# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # recursion to find out if find two
        flag = True
        ans = 0
        
        def recr(node):
            nonlocal ans, flag
            
            if not node or not flag:
                return 0
            
            condition = 0            
            if node.val == p.val or node.val == q.val:
                condition += 1
            
            left = recr(node.left)
            right = recr(node.right)
            
            condition += left + right
            
            if condition >= 2:
                flag = False
                ans = node
                return 0
            else:
                return condition
            
        recr(root)
        return ans
