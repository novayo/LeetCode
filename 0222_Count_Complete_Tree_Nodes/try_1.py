# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root == None: return 0
        
        height = 0
        def get_height(node):
            nonlocal height
            if node == None:
                return
            height += 1
            get_height(node.left)
            
        miss, flag = 0, True
        def dfs_from_right_to_left(node, h=0):
            nonlocal flag
            nonlocal miss
            
            if node == None:
                miss += 1
                return
            if h == height-1:
                flag = False
            
            if flag:
                dfs_from_right_to_left(node.right, h+1)
            if flag:
                dfs_from_right_to_left(node.left, h+1)
            
        
        get_height(root)
        dfs_from_right_to_left(root)
        
        return (2**height - 1) - miss
