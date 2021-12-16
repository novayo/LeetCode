# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        
        def dfs(node):
            if not node:
                return 0
            
            cur_sum = 0
            if low <= node.val <= high:
                cur_sum += node.val
                
            if node.val > low:
                cur_sum += dfs(node.left)
            
            if node.val < high:
                cur_sum += dfs(node.right)
            
            return cur_sum
        
        return dfs(root)