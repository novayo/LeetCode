# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(node, _min, _max):
            if node == None:
                return True
            if node.val < _min or node.val > _max:
                return False
            return dfs(node.left, _min, node.val-1) and dfs(node.right, node.val+1, _max)
            
        return dfs(root, -float('inf'), float('inf'))
