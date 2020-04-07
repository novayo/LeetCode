# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def preorder(node, _sum=0):
            ans = 0
            if node.left == None and node.right == None:
                return _sum*10+node.val
            
            if node.left:
                ans += preorder(node.left, _sum*10+node.val)
            
            if node.right:
                ans += preorder(node.right, _sum*10+node.val)
            return ans
        
        if not root: return 0
        return preorder(root)
        
