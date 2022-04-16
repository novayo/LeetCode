# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        '''
        bst
        '''
        
        def dfs(node, l, r):
            if l > r:
                return None
            if not node:
                return None
            
            if r < node.val:
                return dfs(node.left, l, r)
            elif l > node.val:
                return dfs(node.right, l, r)
            else:
                node.left = dfs(node.left, l, node.val-1)
                node.right = dfs(node.right, node.val+1, r)
                return node
        
        return dfs(root, low, high)
        
