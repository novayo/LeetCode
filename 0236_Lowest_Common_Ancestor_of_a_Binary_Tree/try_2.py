# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        子樹有找到回傳True，左右都找到則為LCA
        '''
        ans = None
        flag = False
        
        def bottom_up(node):
            nonlocal ans, flag
            if flag:
                return False
            
            if not node:
                return False
            
            selfnode = node == p or node == q
            left = bottom_up(node.left)
            right = bottom_up(node.right)
            
            if left == right == True or left == selfnode == True or right == selfnode == True:
                ans = node
                flag = True
            
            return left or right or selfnode
        
        bottom_up(root)
        return ans